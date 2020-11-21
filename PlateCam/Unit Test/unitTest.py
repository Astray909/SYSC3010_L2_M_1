'''
Unit Test file, run this to test all system functions
'''

import unittest
import time
from sense_hat import SenseHat

import os,sys,inspect
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
        writeTS("BVHV966", "", "")
        self.assertEqual(readPlate(), "BVHV966", "Should be the same") #Test write to TS, compare value to known value

    def test_plate_reading(self):
        self.assertEqual(read_plate(), "BVHV966", "Should be BVHV966") #Test plate reading algorithm, compare against konwn value

    def test_LED(self):
        sense.set_pixels(RED)
        time.sleep(1)
        sense.set_pixels(GREEN)
        time.sleep(1)
        sense.set_pixels(BLUE)
        time.sleep(1)
        sense.set_pixels(NONE)
        self.assertEqual(1, 1, "LED pass") #Cycles through RGB colours

if __name__ == '__main__':
    unittest.main()