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

#this variable is used to check if the entries in thingspeak are within the 15 second interval
timebefore = 0

#Initializes connection with database and intializes tables in the database
dbconnect = sqlite3.connect("parkinglot.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
cursor.execute('''create table IF NOT EXISTS CarDosier (PlateNumber TEXT, EntryTime TEXT, ExitTime TEXT, hasPaid INTEGER, Amount DOUBLE)''');
cursor.execute('''create table IF NOT EXISTS DoorStatus (GateStatus INTEGER)''');
cursor.execute('''create table IF NOT EXISTS ParkingSheet (LotID INTEGER, FloorID INTEGER, FloorSpots INTEGER, SpotID INTEGER, Status INTEGER)''');

#pulls the entrytime from thingspeak and breaks down the input into our designated format (e.x. 2020-11-19 21:16:42)
def date_time(dt):
    date = dt.split('T')[0]
    time = dt.split('T')[1]
    time1 = time.split('Z')[0]
    datetime = date + ' ' + time1
    return datetime

#This function will take the entrytime from the database and compare that time to the current time to calculate how much the person owes
def compare_time(entrytime):
    #Gets the current time to compare to excluding microseconds
    x = datetime.datetime.now().replace(microsecond=0)
    
    #Splits the date and time apart and then further seperates to match the python datetime function
    d1, t1 = entrytime.split(' ')[0], entrytime.split(' ')[1]
    d2 = d1.split('-')
    t2 = t1.split(':')
    
    #Compiles all the splits to match the correct datetime format (e.x. datetime.datetime(year, month, day, hour, minute, second)
    full = datetime.datetime(int(d2[0]), int(d2[1]), int(d2[2]), int(t2[0]), int(t2[1]), int(t2[2]))
    
    #returns the difference in seconds
    difference = (x-full).seconds
    
    return difference

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
        
        #Individually checks all entries 
        plate_number = (data['feeds'][0]['field1'])
        entry_time = (data['feeds'][0]['field2'])
        door_status = (data['feeds'][0]['field3'])
        
        #For the parking entries, I check the feeds list and pull the data from each field
        lot_ID = (data['feeds'][0]['field4'])
        floor_ID = (data['feeds'][0]['field5'])
        floor_spots = (data['feeds'][0]['field6'])
        spot_ID = (data['feeds'][0]['field7'])
        state = (data['feeds'][0]['field8'])
        
        print (plate_number)
        print (entry_time)
        print (door_status)
        print (lot_ID)
        print (floor_ID)
        print (floor_spots)
        print (spot_ID)
        print (state)
        GPIO.output(led2,1)
        time.sleep(5)
        GPIO.output(led2,0)
        time.sleep(5)

        TS.close()
      
    except:
        print ("connection failed")