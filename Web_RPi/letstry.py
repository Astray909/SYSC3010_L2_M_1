import datetime
date = "2020-11-20T15:51:10Z"
def date_time(dt):
    date = dt.split('T')[0]
    time = dt.split('T')[1]
    time1 = time.split('Z')[0]
    #These statements will edit the time to the correct time
    time2 = time1.split(':')
    time2[0] = int(time2[0])
    time2[0] -= 5
    time2[0] = str(time2[0])
    time3 = time2[0] + ':' + time2[1] + ':' + time2[2]
    datetime = date + ' ' + time3
    return datetime
date1 = date_time(date)
