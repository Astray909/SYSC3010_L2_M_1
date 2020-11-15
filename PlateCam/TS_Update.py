from sense_hat import SenseHat
import httplib
import urllib
import time

labkey = "UPJ636UNXXEE2IIG"

def write(plate, time):
    while True:
        params = urllib.urlencode({'field1': plate, 'field2': time, 'key':labkey }) 
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