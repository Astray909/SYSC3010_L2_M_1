"""
writes to desired TS channel with plate and timestamp information
"""

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
    fieldFour = readSpots(4)
    fieldFive = readSpots(5)
    fieldSix = readSpots(6)
    fieldSeven = readSpots(7)
    fieldEight = readSpots(8)
    while True: #relays all existing fields and send them with the updated fields
        params = urllib.urlencode(
            {
                "field1": fieldOne,
                "field2": fieldTwo,
                "field3": fieldThree,
                "field4": fieldFour,
                "field5": fieldFive,
                "field6": fieldSix,
                "field7": fieldSeven,
                "field8": fieldEight,
                "key": WRITE_API_KEY,
            }
        )
        headers = {
            "Content-typZZe": "application/x-www-form-urlencoded",
            "Accept": "text/plain",
        }
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            #print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break


def write(plate, time):
    writeTS(plate, time, "00")  # writes plate number, time, and stop signal


def updateStatus():
    writeTS("", "", "00")  # writes stop signal


def updateStatusto1():
    writeTS("", "", "A1")  # writes start signal


def stopCam():
    writeTS("", "", "XX")  # writes emergency stop signal


def writeToTS():
    # print("Camera On")
    now = datetime.now().replace(microsecond=0)
    current_time = now

    plateNo = read_plate()

    if plateNo == "error10086":  # check for no plate found error
        print("No plate found, trying again")
        return
    else:
        write(plateNo, current_time)
