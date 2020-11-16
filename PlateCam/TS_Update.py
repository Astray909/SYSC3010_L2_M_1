import httplib
import urllib
import time
from datetime import datetime

from keys import *
#from keys2 import *

from TS_Update import *
from TS_Download import *
from Plate_Reading import *

WRITE_API_KEY = WRITE_KEY()

def write(plate, time):
    while True:
        params = urllib.urlencode({'field1': plate, 'field2': time, 'field3': "00", 'key':WRITE_API_KEY }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

def updateStatus():
    while True:
        params = urllib.urlencode({'field3': "00",'key':WRITE_API_KEY }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

def updateStatusto1():
    while True:
        params = urllib.urlencode({'field3': "A1",'key':WRITE_API_KEY }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

def stopCam():
    while True:
        params = urllib.urlencode({'field3': "XX",'key':WRITE_API_KEY }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

def writeToTS():
    print("yes")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    plateNo = read_plate()
    
    if plateNo == "error10086":
        print("No plate found, trying again")
        return
    else:
        write(plateNo, current_time)