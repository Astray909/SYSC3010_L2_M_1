"""
reads and returns information from TS channel field3, which is used for gate status indication
"""

import urllib2
import json

from keys import *

#from keys2 import *

READ_API_KEY = READ_KEY()
CHANNEL_ID = ID()


def retrieve():
    conn = urllib2.urlopen(
        "http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s"
        % (CHANNEL_ID, READ_API_KEY)
    )

    response = conn.read()
    print "http status code=%s" % (conn.getcode())
    data = json.loads(response)
    conn.close()
    return data


def read():
    data = retrieve()
    return data["field3"]


def readPlate():
    data = retrieve()
    return data["field1"]


def readSpots(config):
    fieldid = "field" + str(config)
    data = retrieve()
    return data[fieldid]
