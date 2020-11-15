import urllib2
import json

READ_API_KEY='QI5S8B9MQZUNI1YV'
CHANNEL_ID=1169779

def read():
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))

    response = conn.read()
    print "http status code=%s" % (conn.getcode())
    data=json.loads(response)
    print data['field1'] ,data['created_at']
    print data['field2'] ,data['created_at']
    print data['field3'] ,data['created_at']
    conn.close()