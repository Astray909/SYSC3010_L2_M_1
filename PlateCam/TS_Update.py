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

def writeTS(fieldOne, fieldTwo, fieldThree):
    while True:
        params = urllib.urlencode({'field1': fieldOne, 'field2': fieldTwo, 'field3': fieldThree, 'key':WRITE_API_KEY }) 
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

def write(plate, time):
    writeTS(plate, time, "00")

def updateStatus():
    writeTS("", "", "00")

def updateStatusto1():
    writeTS("", "", "A1")

def stopCam():
    writeTS("", "", "XX")

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