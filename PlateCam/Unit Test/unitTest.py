"""
Unit Test file, run this to test all system functions
"""

import unittest
import time
from sense_hat import SenseHat

import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from TS_Update import *
from main import *
from Plate_Reading import *
from TS_Download import *
from TS_Update import *

sense = SenseHat()

G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
X = (0,0,0)
P = (255,105, 180)

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

RED = [
R,R,R,R,R,R,R,R,
R,R,R,R,R,R,R,R,
R,R,R,R,R,R,R,R,
R,R,R,R,R,R,R,R,
R,R,R,R,R,R,R,R,
R,R,R,R,R,R,R,R,
R,R,R,R,R,R,R,R,
R,R,R,R,R,R,R,R
]

GREEN = [
G,G,G,G,G,G,G,G,
G,G,G,G,G,G,G,G,
G,G,G,G,G,G,G,G,
G,G,G,G,G,G,G,G,
G,G,G,G,G,G,G,G,
G,G,G,G,G,G,G,G,
G,G,G,G,G,G,G,G,
G,G,G,G,G,G,G,G
]

BLUE = [
B,B,B,B,B,B,B,B,
B,B,B,B,B,B,B,B,
B,B,B,B,B,B,B,B,
B,B,B,B,B,B,B,B,
B,B,B,B,B,B,B,B,
B,B,B,B,B,B,B,B,
B,B,B,B,B,B,B,B,
B,B,B,B,B,B,B,B
]

class TestSum(unittest.TestCase):
    def test_TS_write(self):
        print("Beginning ThingSpeak writing integration test")
        time.sleep(5)
        writeTS("TEST", "", "")
        self.assertEqual(
            readPlate(), "TEST", "Should be the same"
        )  # Test write to TS, compare value to known value

    def test_read_TS3(self):
        print("Beginning ThingSpeak reading integration test")
        time.sleep(5)
        writeTS("", "", "TEST")
        self.assertEqual(
            read(), "TEST", "Should be the same"
        )  # Test read from TS, compare value to known value

    def test_plate_reading(self):
        print("Beginning plate recognizing unit test")
        self.assertEqual(
            read_plate(), "BVHV966", "Should be BVHV966"
        )  # Test plate reading algorithm, compare against konwn value

    def test_GUI(self):
        print("Beginning GUI integration test")
        time.sleep(5)
        writeTS("Testing GUI", "", "")
        self.assertEqual(1, 1, "GUI test")  # GUI test

    def test_LED(self):
        print("Beginning LED matrix unit test")
        sense.set_pixels(RED)
        time.sleep(3)
        sense.set_pixels(GREEN)
        time.sleep(3)
        sense.set_pixels(BLUE)
        time.sleep(3)
        sense.set_pixels(NONE)
        self.assertEqual(1, 1, "LED pass")  # Cycles through RGB colours


if __name__ == "__main__":
    unittest.main()
