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

def date_time(dt):
    date = dt.split('T')[0]
    time = dt.split('T')[1]
    time1 = time.split('Z')[0]
    datetime = date + ' ' + time1
    return datetime

def calculate_amount(entrytime):
    x = datetime.datetime.now().replace(microsecond=0)
    d1, t1 = entrytime.split(' ')[0], entrytime.split(' ')[1]
    d2 = d1.split('-')
    t2 = t1.split(':')
    full = datetime.datetime(int(d2[0]), int(d2[1]), int(d2[2]), int(t2[0]), int(t2[1]), int(t2[2]))
    y = (x-full).seconds
    amount = round(y*(0.05*(1/60)),2)
    if amount > 20:
        amount = 20
    return amount

while True:
  TS = urllib.request.urlopen("https://api.thingspeak.com/channels/1169779/feeds.json?results=1")
  GPIO.output(led1, 1)
  time.sleep(5)
  GPIO.output(led1, 0)

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