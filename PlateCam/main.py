from TS_Update import *
from TS_Download import *
from Plate_Reading import *

import time
import os
import json
from datetime import datetime

def writeToTS():
    print("yes")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    plateNo = read_plate()
    
    if plateNo == 10086:
        print("No plate found, trying again")
        return
    else:
        write(plateNo, current_time)

if __name__ == "__main__":
    while True:
        gateStatus = read()
        print(gateStatus)
        if gateStatus == "A1" or gateStatus == "B1" or gateStatus == "c1":
            writeToTS()
        time.sleep(1)