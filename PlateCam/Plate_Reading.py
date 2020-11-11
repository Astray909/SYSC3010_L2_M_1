import time
import os
import picamera
import json
from openalpr import Alpr

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('plate.jpg')

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "test.jpg"
    abs_file_path = os.path.join(script_dir, rel_path)

    alpr = Alpr("us", "/etc/openalpr/openalp.conf", "/usr/share/openalpr/runtime_data")
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)
    results = alpr.recognize_file(abs_file_path)
    print(results["results"][0]["plate"])
    print(results["results"][0]["confidence"])
    alpr.unload()
