import urllib2
import json
from keys import *

READ_API_KEY = 'QI5S8B9MQZUNI1YV'
CHANNEL_ID = '116979'

def read():
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))

    response = conn.read()
    print "http status code=%s" % (conn.getcode())
    data=json.loads(response)
    conn.close()
    return data['field3']