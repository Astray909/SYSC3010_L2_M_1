from Tkinter import *
import datetime

from TS_Download import *

root = Tk()

lab = Label(root)
lab.pack()

def display():
    plateNo = read()
    time = datetime.datetime.now().strftime(plateNo)
    lab.config(text=time)
    root.after(1000, display)

display()

root.mainloop()