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
    write(plateNo, current_time)
    updateStatus()

if __name__ == "__main__":
    while True:
        gateStatus = read()
        print(gateStatus)
        if gateStatus > 0:
            writeToTS()
        time.sleep(1)