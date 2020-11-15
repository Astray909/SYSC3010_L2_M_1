import urllib2
import json

READ_API_KEY='T8JSN8K6KFPDN1I1'
CHANNEL_ID=1172874

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