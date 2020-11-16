import time
import os
import picamera
import json
from openalpr import Alpr
from datetime import datetime

def read_plate():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture('plate.jpg')

        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        #rel_path = "test.jpg"
        rel_path = "plate.jpg"
        abs_file_path = os.path.join(script_dir, rel_path)

        alpr = Alpr("us", "/etc/openalpr/openalp.conf", "/usr/share/openalpr/runtime_data")
        if not alpr.is_loaded():
            print("Error loading OpenALPR")
            sys.exit(1)
        results = alpr.recognize_file(abs_file_path)
        #print(json.dumps(results, indent = 4))

        try:
            plateNo = results["results"][0]["plate"]
            print(plateNo)
            print(results["results"][0]["confidence"])
        except:
            plateNo = "error10086"

        alpr.unload()

        return plateNo
