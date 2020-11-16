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
        if gateStatus == "XX":
            exit()
        if gateStatus != "00" and gateStatus != "11":
            writeToTS()
        time.sleep(1)