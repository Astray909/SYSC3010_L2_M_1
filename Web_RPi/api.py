#import libraries
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

led1 = 4
led2 = 17
led3 = 27
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)

while True:
  TS = urllib.request.urlopen("https://api.thingspeak.com/channels/1169779/feeds.json?results=1")

  response = TS.read()
  data=json.loads(response)
  pprint(data)
  print (data['feeds'][0]['field4'])
  time.sleep(5)
  TS.close()    