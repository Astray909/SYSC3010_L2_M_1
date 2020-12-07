"""
This program will take a picture and look for a license plate,
will return the plate number and time if a plate is found
and successfully read
"""

from sense_hat import SenseHat
import time
import os
import picamera
import json
from openalpr import Alpr
from datetime import datetime

sense = SenseHat()

G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255, 255, 255)
X = (0, 0, 0)
P = (255, 105, 180)

NONE = [
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X
]

green_arrow = [
X,X,X,G,G,X,X,X,
X,X,G,G,G,G,X,X,
X,G,X,G,G,X,G,X,
G,X,X,G,G,X,X,G,
X,X,X,G,G,X,X,X,
X,X,X,G,G,X,X,X,
X,X,X,G,G,X,X,X,
X,X,X,G,G,X,X,X
]

yellow_circle = [
X,X,Y,Y,Y,Y,X,X,
X,Y,Y,Y,Y,Y,Y,X,
Y,Y,Y,Y,Y,Y,Y,Y,
Y,Y,Y,Y,Y,Y,Y,Y,
Y,Y,Y,Y,Y,Y,Y,Y,
Y,Y,Y,Y,Y,Y,Y,Y,
X,Y,Y,Y,Y,Y,Y,X,
X,X,Y,Y,Y,Y,X,X
]

red_cross = [
R,R,X,X,X,X,R,R,
X,R,R,X,X,R,R,X,
X,X,R,R,R,R,X,X,
X,X,X,R,R,X,X,X,
X,X,X,R,R,X,X,X,
X,X,R,R,R,R,X,X,
X,R,R,X,X,R,R,X,
R,R,X,X,X,X,R,R
]

def read_plate():
    with picamera.PiCamera() as camera:
        sense.set_pixels(yellow_circle)  # signal the driver with yellow circle
        camera.resolution = (1024, 768)  # XGA resolution for faster processing
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture("plate.jpg")

        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        #rel_path = "test.jpg"  # testing image
        rel_path = "plate.jpg" #picture captured by PiCamera
        abs_file_path = os.path.join(
            script_dir, rel_path
        )  # combines file and directory

        alpr = Alpr(
            "us", "/etc/openalpr/openalp.conf", "/usr/share/openalpr/runtime_data"
        )
        if not alpr.is_loaded():
            print("Error loading OpenALPR")
            sys.exit(1)
        results = alpr.recognize_file(abs_file_path)
        # print(json.dumps(results, indent = 4))

        try:
            plateNo = results["results"][0]["plate"]
            print(plateNo)
            sense.set_pixels(green_arrow)  # signal the driver with green arrow
            #print(results["results"][0]["confidence"])
        except:
            # sense.set_pixels(red_cross) #signal the driver with red cross
            plateNo = "error10086"  # returns an error code if no plate was found

        alpr.unload()  # closes alpr, prevents resource leakage

        return plateNo
