import urllib.request
import threading
import json
import datetime


# Define a function that will post on server every 15 Seconds
WRITE_API_KEY = 'UPJ636UNXXEE2IIG'
plate = 'L1V3A6'
time = datetime.datetime.now().replace(microsecond=0)

def thingspeak_post(fieldOne, fieldTwo):
    while True:
        params = urllib.urlencode(
            {
                "field1": fieldOne,
                "field2": fieldTwo,
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
    
if __name__ == '__main__':
    thingspeak_post(plate, time)