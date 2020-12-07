"""
main program
"""

from sense_hat import SenseHat
from TS_Update import *
from TS_Download import *
from Plate_Reading import *

import time
import os
import json
from datetime import datetime

import unicodedata

sense = SenseHat()

if __name__ == "__main__":
    while True:
        gateStatus = read()  # constantly poll from TS channel for update
        print(gateStatus)
        if gateStatus == "XX":
            exit()
        if (
            gateStatus != None
            and gateStatus.isalnum()
            and gateStatus != "00"
            and gateStatus != "YES"
            and gateStatus != "NO"
        ):
            writeToTS()
        time.sleep(1)  # sleep timer to compensate for TS update interval
        sense.clear()  # clear sensehat
