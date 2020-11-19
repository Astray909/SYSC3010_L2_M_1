'''
main program
'''

from TS_Update import *
from TS_Download import *
from Plate_Reading import *

import time
import os
import json
from datetime import datetime

if __name__ == "__main__":
    while True:
        gateStatus = read() #constantly poll from TS channel for update
        print(gateStatus)
        if gateStatus == "XX":
            exit()
        if gateStatus == "A1" or gateStatus == "B1" or gateStatus == "C1":
            writeToTS()
        time.sleep(1) #sleep timer to compensate for TS update interval
