import urllib2
import json

from keys import *
#from keys2 import *

READ_API_KEY = READ_KEY()
CHANNEL_ID = ID()

def read():
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))

    response = conn.read()
    print "http status code=%s" % (conn.getcode())
    data=json.loads(response)
    conn.close()
    return data['field3']