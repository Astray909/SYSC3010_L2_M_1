from TS_Update import *
from TS_Download import *
from Plate_Reading import *

import time
import os
import json
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

plateNo = read_plate()

write(plateNo, current_time)