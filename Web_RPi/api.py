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
cursor.execute('''create table IF NOT EXISTS CarDosier (PlateNumber TEXT, EntryTime TEXT, ExitTime TEXT, hasPaid INTEGER, Amount DOUBLE)''');
cursor.execute('''create table IF NOT EXISTS DoorStatus (GateStatus INTEGER)''');
cursor.execute('''create table IF NOT EXISTS ParkingSheet (LotID INTEGER, FloorID INTEGER, FloorSpots INTEGER, SpotID INTEGER, Status INTEGER)''');

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
    time2[0] = int(time2[0])
    time2[0] -= 5
    time2[0] = str(time2[0])
    time3 = time2[0] + ':' + time2[1] + ':' + time2[2]
    datetime = date + ' ' + time3
    return datetime

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

#
def calculate_amount(time):
    amount = round(time*(0.05*(1/60)),2)
    if amount > 20:
        amount = 20
    return amount

while True:
    TS = urllib.request.urlopen("https://api.thingspeak.com/channels/1169779/feeds.json?results=1")
    GPIO.output(led1, 1)
    time.sleep(5)
    GPIO.output(led1, 0)

    try:
        response = TS.read()
        data=json.loads(response)
        
        #checks for any feeds that have come up
        for i in data['feeds']:
            
            #if the input time is between the time interval then the function will go through
            time_interval = date_time(data['feeds'][i]['created_at'])
            if (0 <= compare_time(time_interval) <= 15):
                
                #Individually checks all entries 
                plate_number = (data['feeds'][i]['field1'])
                entry_time = (data['feeds'][i]['field2'])
                
                
                door_status = (data['feeds'][i]['field3'])
        
                #For the parking entries, I check the feeds list and pull the data from each field
                lot_ID = (data['feeds'][i]['field4'])
                floor_ID = (data['feeds'][i]['field5'])
                floor_spots = (data['feeds'][i]['field6'])
                spot_ID = (data['feeds'][i]['field7'])
                state = (data['feeds'][i]['field8'])
                
        
        GPIO.output(led2,1)
        time.sleep(5)
        GPIO.output(led2,0)
        time.sleep(5)

    TS.close()      
    except:
        print ("connection failed")