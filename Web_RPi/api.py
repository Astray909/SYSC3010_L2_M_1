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
    CREATE TABLE IF NOT EXISTS DoorStatus (GateStatus TEXT)''');

#setups up the parking management table and ensures null values aren't added and are not duplicates
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ParkingSheet (
    LotID INTEGER,
    FloorID INTEGER,
    FloorSpots INTEGER,
    SpotID INTEGER,
    Status Text)''');

#writes gate codes to the Thingspeak channel
def write_to_TS(field3):
    URl='https://api.thingspeak.com/update?api_key='
    KEY='UPJ636UNXXEE2IIG'
    HEADER='&field3={}'.format(field3)
    NEW_URL=URl+KEY+HEADER
    data=urllib.request.urlopen(NEW_URL)

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
    split_time = dtime.split(':')
    fixed_time = datetime.datetime.combine(datetime.date.today(),
                                  datetime.time(int(float(split_time[0])), int(float(split_time[1])), int(float(split_time[2]))))
    return fixed_time

#This function will take the entrytime from the database and compare that time to the current time to calculate how much the person owes
def compare_time(time):
    #Gets the current time to compare to excluding microseconds
    current = datetime.datetime.now().replace(microsecond=0)
    
    #Splits the date and time apart and then further seperates to match the python datetime function
    d1, t1 = time.split(' ')[0], time.split(' ')[1]
    d2 = d1.split('-')
    t2 = t1.split(':')
    
    #Compiles all the splits to match the correct datetime format (e.x. datetime.datetime(year, month, day, hour, minute, second)
    full = datetime.datetime(int(d2[0]), int(d2[1]), int(d2[2]), int(t2[0]), int(t2[1]), int(t2[2]))
    
    #returns the difference in seconds
    difference = (current-full).seconds
    return difference

#calculates the amount that a customer owes for their parking space, the inserted value is alwasys a car's entry time
#The price will change to $20 if the calculated amount is more than $20 like a regular parking lot
def calculate_amount(time):
    
    #sends the entry time to the compare_time function to calculate the seconds a car has been parked
    spent_time = compare_time(time)
    
    #applies the second based rate
    amount = round(spent_time*(0.05*(1/60)),2)
    if amount >= 20:
        amount = 20.00
    return amount

while True:
    TS = urllib.request.urlopen("https://api.thingspeak.com/channels/1169779/feeds.json?results=1")
    #signals LED that the connection was successful
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(led1, GPIO.LOW)

    response = TS.read()
    data=json.loads(response)
    
    #updates the amount owed for any cars that are currently parked in the lot
    try:
        cursor.execute("""SELECT * from CarDosier""")
        records = cursor.fetchall()
        for row in records:
            update_sum = calculate_amount(row['EntryTime'])
            ID = row['PlateNumber']
            cursor.execute('''UPDATE CarDosier Set Amount = ? Where PlateNumber = ?''', (update_sum, ID));
            dbconnect.commit();
    except:
        pass
        
    #checks for any feeds that have come up
    index = 0
    for i in range(len(data['feeds'])):
            
        #if the input time is between the time interval then the function will go through
        creation_time = (data['feeds'][index]['created_at'])
        time_interval = date_time(creation_time)
        interval = compare_time(time_interval)
        #this statement checks if the last few entry points fall within the 15 second window so we can track any new information
        if (0 <= interval <= 15):
            
            #Individually checks all entries 
            plate_number = (data['feeds'][index]['field1'])
            entry_time = (data['feeds'][index]['field2'])
            door_status = (data['feeds'][index]['field3'])
            
            #this exception block is used for if a car is entering for the first time then these statements will be passed and go into the car entry lines afterwards
            #if a car is trying to exit and is already logged in the database then these statements will be used
            try:    
                #checks if there is a door status code in the Thingspeak channel, specifically for when the car wishes to exit
                if(door_status != None and door_status != ""):
                    #checks for specific code as to proct the system to see if someone is exiting or entering
                    if(door_status == "00"):
                        cursor.execute('''SELECT * FROM CarDosier''');
                        for row in cursor:
                            #searches the database for a car with the matching plate number
                            if(row['PlateNumber'] == plate_number):
                                #if the person hasn't paid then we ask if they'd like to pay now and exit the lot
                                if(row['hasPaid'] == 0):
                                    amount = str(row['Amount'])
                                    print("Hello and Welcome to the A.P.A. Managament System! We just found your car on our registry and currently")
                                    print("$"+amount+" is how much you owe")
                                    print("Would you like to pay now? [Y/N]")
                                    answer = input()
                                    if(answer == "Y" or answer =="y"):
                                        present = datetime.datetime.now().replace(microsecond=0)
                                        #update the database to say that the person has paid and the time they exit
                                        cursor.execute('''UPDATE CarDosier SET hasPaid = 1, ExitTime = ? WHERE PlateNumber=?''', (present, plate_number));
                                        dbconnect.commit();
                                        print("You've successfully paid for your spot and are ready to exit the lot when ready!")
                                        write_to_TS('YES');
                                    else:
                                        print("It's okay you can pay whenever you're ready later on");
                                        write_to_TS('NO')
                                if(row['hasPaid'] == '1'):
                                    write_to_TS('YES');
            except:
                pass
                                
            #use of the exception protocol is to allow the program to continue even if it tries to add a car that has already been registered
            try:
                #ensures that there are no empty entries being entered into the database
                if(plate_number != None and plate_number != ""):
                    if(entry_time != None and entry_time != ""):
                        #inserts new car into database
                        cursor.execute('''INSERT INTO CarDosier (PlateNumber, EntryTime, ExitTime, hasPaid, Amount) VALUES (?, ?, '0', 0, 0)''', (plate_number, entry_time));
                        dbconnect.commit();
                        #prompts the gate to open for the user
                        write_to_TS('YES')
            except:
                pass
                
            #For the parking entries, I check the feeds list and pull the data from each field
            lot_ID = (data['feeds'][index]['field4'])
            floor_ID = (data['feeds'][index]['field5'])
            floor_spots = (data['feeds'][index]['field6'])
            spot_ID = (data['feeds'][index]['field7'])
            state = (data['feeds'][index]['field8'])
            
            try:
                #ensures that each entry is not null/None
                if(lot_ID != None and floor_ID != None and floor_spots != None and spot_ID != None and state != None):
                    cursor.execute('''INSERT into ParkingSheet (LotID, FloorID, FloorSpots, SpotID, Status) VALUES (?, ?, ?, ?, ?)''',
                            (lot_ID, floor_ID, floor_spots, spot_ID, state));
                    dbconnect.commit();
            except:
                lot_ID = None and ""
                floor_ID = None and ""
                floor_spots = None and ""
                spot_ID = None and ""
                state = None and ""
            
            #used in ensuring that the loop checks all entries in the feed
            index+=1
                        
    #signals the second LED that the information was correctly stored
    GPIO.output(led2,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(led2, GPIO.LOW)
    time.sleep(5)

    TS.close()