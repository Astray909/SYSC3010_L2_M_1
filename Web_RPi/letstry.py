import datetime
date = "2020-11-20T15:51:10Z"
def date_time(dt):
    date = dt.split('T')[0]
    time = dt.split('T')[1]
    time1 = time.split('Z')[0]
    datetime = date + ' ' + time1
    return datetime
date1 = date_time(date)
