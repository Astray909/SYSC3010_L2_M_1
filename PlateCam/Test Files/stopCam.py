'''
debugging script to stop PlateCam
'''
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from TS_Update import *

print("wrote XX to field3") #writes XX to field3, code for emergency stop

stopCam()
