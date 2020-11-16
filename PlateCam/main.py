from TS_Update import *
from TS_Download import *
from Plate_Reading import *

import time
import os
import json
from datetime import datetime

if __name__ == "__main__":
    while True:
        gateStatus = read()
        print(gateStatus)
        if gateStatus == "A1" or gateStatus == "B1" or gateStatus == "c1":
            writeToTS()
        time.sleep(1)