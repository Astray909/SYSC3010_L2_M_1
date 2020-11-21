#!/usr/bin/env python3
import RPi.GPIO as GPIO
import urllib.request
import time
import sqlite3
import json
import threading
import datetime

#Setting API in order to read from Thingspeak
READ_API_KEY='QI5S8B9MQZUNI1YV'
CHANNEL_ID='1169779'

#Setup's the GPIO pins on the Raspberry Pi to interact with the LED's
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led1 = 4
led2 = 17
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)

#Initializes connection with database and intializes tables in the database
dbconnect = sqlite3.connect("parkinglot.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();

#creates a table that ensure there are no duplicate cars (plate numbers) being entered
cursor.execute('''
    CREATE TABLE IF NOT EXISTS CarDosier (
    PlateNumber TEXT UNIQUE,
    EntryTime TEXT,
    ExitTime TEXT,
    hasPaid INTEGER,
    Amount DOUBLE)''');

#special field to enable requests
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DoorStatus (GateStatus INTEGER)''');

#setups up the parking management table and ensures null values aren't added and are not duplicates
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ParkingSheet (
    LotID INTEGER NOT NULL,
    FloorID INTEGER NOT NULL,
    FloorSpots INTEGER NOT NULL,
    SpotID INTEGER NOT NULL,
    Status INTEGER NOT NULL)''');

#pulls the entrytime from thingspeak formatted as (2020-11-20T17:55:49Z)
#and breaks down the input into our designated format (2020-11-19 21:16:42)
#due to the creation field not taking into account for timezones, we take off 5 hours to correct the time
def date_time(dt):
    #These statements will split the intial given statement
    date = dt.split('T')[0]
    time = dt.split('T')[1]
    time1 = time.split('Z')[0]
    
   #These statements will edit the time to the correct time
    time2 = time1.split(':')
    
    #Corrects the hour by decreasing the hour by 5
    time2[0] = int(time2[0])
    time2[0] -= 5
    
    #if the hour is within the negatives we will correct it to the right day and hour
    if (time2[0] < 0):
        time2[0] += 24
        
        #adjusts the date of the given time
        date1 = date.split('-')
        date1[2] = int(date1[2])
        date1[2] -= 1
        date1[2] = str(date1[2])
        
        #reassembles the date accordingly
        date = date1[0] + '-' + date1[1] + '-' + date1[2]
        
    time2[0] = str(time2[0])
    
    #reassembles the time, after changes are made, in the desired format
    time3 = time2[0] + ':' + time2[1] + ':' + time2[2]
    datetime = date + ' ' + time3
    return datetime

#function to apppend a date to the entry time assuming that then entry is the day of
def date_entry(dtime):
    time1 = dtime.split(':')
    x = datetime.datetime.combine(datetime.date.now(),
                                  datetime.time(time1[0], time1[1], time1[2]))
    return x

#This function will take the entrytime from the database and compare that time to the current time to calculate how much the person owes
def compare_time(time):
    #Gets the current time to compare to excluding microseconds
    x = datetime.datetime.now().replace(microsecond=0)
    
    #Splits the date and time apart and then further seperates to match the python datetime function
    d1, t1 = time.split(' ')[0], time.split(' ')[1]
    d2 = d1.split('-')
    t2 = t1.split(':')
    
    #Compiles all the splits to match the correct datetime format (e.x. datetime.datetime(year, month, day, hour, minute, second)
    full = datetime.datetime(int(d2[0]), int(d2[1]), int(d2[2]), int(t2[0]), int(t2[1]), int(t2[2]))
    
    #returns the difference in seconds
    difference = (x-full).seconds
    return difference

#calculates the amount that a customer owes for their parking space, the inserted value is alwasys a car's entry time
#The price will change to $20 if the calculated amount is more than $20 like a regular parking lot
def calculate_amount(time):
    
    #sends the entry time to the compare_time function to calculate the seconds a car has been parked
    x = compare_time(time)
    
    #applies the second based rate
    amount = round(x*(0.05*(1/60)),2)
    if amount >= 20:
        amount = 20
    return amount

while True:
    TS = urllib.request.urlopen("https://api.thingspeak.com/channels/1169779/feeds.json?results=1")
    #signals LED that the connection was successful
    GPIO.output(led1, 1)
    time.sleep(5)
    GPIO.output(led1, 0)

    response = TS.read()
    data=json.loads(response)
    
    #updates the amount owed for any cars that are currently parked in the lot
    cursor.execute("""SELECT * from CarDosier""")
    records = cursor.fetchall()
    for row in records:
        row[4] = calculate_amount(row[2])
        
    #checks for any feeds that have come up
    z = 0
    for i in range(len(data['feeds'])):
            
        #if the input time is between the time interval then the function will go through
        creation_time = (data['feeds'][z]['created_at'])
        time_interval = date_time(creation_time)
        interval = compare_time(time_interval)
        if (0 <= interval <= 15):
                
            #Individually checks all entries 
            plate_number = (data['feeds'][z]['field1'])
            entry_time = (data['feeds'][z]['field2'])
            
            #inserts new car into database
            cursor.execute('''insert into CarDosier (PlateNumber, EntryTime, hasPaid) values (%s, %s, 0)'''
                    % (plate_number, date_entry(entry_time)));
            
            
                    
            door_status = (data['feeds'][z]['field3'])
        
            #For the parking entries, I check the feeds list and pull the data from each field
            lot_ID = (data['feeds'][z]['field4'])
            floor_ID = (data['feeds'][z]['field5'])
            floor_spots = (data['feeds'][z]['field6'])
            spot_ID = (data['feeds'][z]['field7'])
            state = (data['feeds'][z]['field8'])
            cursor.execute('''insert into ParkingSheet (LotID, FloorID, FloorSpots, SpotID, Status) values (%s, %s, %s, %s, %s)'''
                    % (lot_ID, floor_ID, floor_spots, spot_ID, state));
            
            z+=1
                        
        #signals the second LED that the information was correctly stored
        GPIO.output(led2,1)
        time.sleep(5)
        GPIO.output(led2,0)
        time.sleep(5)

    TS.close()      