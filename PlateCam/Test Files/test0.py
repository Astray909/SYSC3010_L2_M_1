"""
Cam off override
"""
import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from TS_Update import *

print("wrote 00 to field 3")
# updateStatusto1()
updateStatus()
