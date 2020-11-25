import httplib
import urllib
import time

key = "UPJ636UNXXEE2IIG"

def thingspeak_post(LotID, FloorID, FloorSpots, SpotID, state, key):
    while True:

        params = urllib.urlencode({'field4':LotID, 'field5':FloorID, 'field6':FloorSpots, 'field7':SpotID, 'field8':state,'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
       
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (response.status, response.reason)
            data = response.read()
            print(data)
            conn.close()
        except:
            print ("connection failed")
        
        break