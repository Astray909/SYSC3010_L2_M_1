"""
Cam on override
"""
import os, sys, inspect

from TS_Update import *

if __name__ == "__main__":
    print("wrote 00 to field 3, gate will now close")
    writeTS("", "", "00")
