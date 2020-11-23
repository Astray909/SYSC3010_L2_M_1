from Tkinter import *
import datetime

from TS_Download import *

root = Tk()

lab = Label(root)
lab.pack()

def display():
    plateNo = readPlate()
    try:
        time = datetime.datetime.now().strftime(plateNo)
    except:
        time = datetime.datetime.now().strftime("No Plate Number")
    lab.config(text=time)
    root.after(1000, display)

display()

root.mainloop()