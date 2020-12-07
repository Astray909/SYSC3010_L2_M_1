"""
Spot read testing
"""
import os, sys, inspect
import time

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from TS_Update import *

from keys import *

def testSpot(five, six):
    fieldOne = ""
    fieldTwo = ""
    fieldThree = ""
    fieldFour = ""
    fieldFive = five
    fieldSix = six
    fieldSeven = ""
    fieldEight = ""
    while True:
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
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break


if __name__ == "__main__":
    testSpot(1, 1)
    time.sleep(10)
    testSpot(2,2)
    time.sleep(10)
    testSpot(1, 0)
    time.sleep(10)
    testSpot(2, 0)
# updateStatus()
