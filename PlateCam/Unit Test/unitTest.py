'''
Unit Test file, run this to test all system functions
'''

import unittest

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from TS_Update import *
from main import *
from Plate_Reading import *
from TS_Download import *
from TS_Update import *

class TestSum(unittest.TestCase):

    def test_TS_write(self):
        writeTS("BVHV966", "", "")
        self.assertEqual(readPlate(), "BVHV966", "Should be the same") #Test write to TS, compare value to known value

    def test_plate_reading(self):
        self.assertEqual(read_plate(), "BVHV966", "Should be BVHV966") #Test plate reading algorithm, compare against konwn value

if __name__ == '__main__':
    unittest.main()