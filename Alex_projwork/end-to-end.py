import http.client
import urllib
import time

key = "7C8703QIH8OGVOP1" # Put your API Key here write to cam's = UPJ636UNXXEE2IIg
def thingspeak_post():
    while True:
        LotID = 1
        FloorID = 1
        FloorSpots = 1
        SpotID = 1
        state = False
        
        params = urllib.parse.urlencode({'field1':LotID, 'field2':FloorID, 'field3':FloorSpots, 'field4':SpotID, 'field5':state,'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
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
if __name__ == "__main__":
        while True:
                thingspeak_post()
                time.sleep(5)