
import RPi.GPIO as GPIO
import urllib.request
import time
import sqlite3
import json
import threading
from pprint import pprint


READ_API_KEY='QI5S8B9MQZUNI1YV'
CHANNEL_ID='1169779'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

dbconnect = sqlite3.connect("parkinglot.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();

led1 = 4
led2 = 17
led3 = 27
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)

while True:
  TS = urllib.request.urlopen("https://api.thingspeak.com/channels/1169779/feeds.json?results=1")
  GPIO.output(led1, 1)
  time.sleep(5)
  GPIO.output(led1, 0)

  response = TS.read()
  data=json.loads(response)
  plate_number = (data['feeds'][0]['field1'])
  entry_time = (data['feeds'][0]['field2'])
  door_status = (data['feeds'][0]['field3'])
  lot_ID = (data['feeds'][0]['field4'])
  floor_ID = (data['feeds'][0]['field5'])
  floor_spots = (data['feeds'][0]['field6'])
  spot_ID = (data['feeds'][0]['field7'])
  state = (data['feeds'][0]['field8'])
  GPIO.output(led2,1)
  time.sleep(5)
  GPIO.output(led2,0)

  TS.close()    