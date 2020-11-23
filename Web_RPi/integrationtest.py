from api.py import *
import unittest
import httplib
import urllib.request
import datetime

def writeTS_1(fieldOne, fieldTwo, fieldThree):
    while True:
        params = urllib.request.urlencode({'field1': fieldOne, 'field2': fieldTwo, 'field3': fieldThree, 'key':UPJ636UNXXEE2IIG }) 
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

class TestSum(unittest.TestCase):

    def test_TS_conn(self):
        print("Starting Thingspeak Connect unit test")
        time = datetime.time.now().replace(microsecond=0)
        writeTS_1("BVHV966", "%s", "") % (time)
        self.assertEqual(plate_number, "BVHV966", "Should be the same")
        self.assertEqual(entry_time, time, "Should be the same")
        
    def test_read_TS3(self):
        print("Beginning ThingSpeak reading unit test")
        time.sleep(5)
        writeTS("", "", "TEST")
        self.assertEqual(read(), "TEST", "Should be the same")

    def test_amount(self):
        print("Beginning amount unit test")
        time.sleep(5)
        date = '2020-11-23 01:32:42'
        amount = calculate_amount(date)
        self.assertEqual(amount, 20, "Amount test") #GUI test

if __name__ == '__main__':
    unittest.main()