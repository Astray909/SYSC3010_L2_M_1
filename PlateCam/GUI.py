from Tkinter import *
import datetime
import time
import sys
import os

from TS_Download import *
import Tkinter as tk

HEIGHT = 500
WIDTH = 900

root = tk.Tk()
root.title("GUI")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
x=40000
sys.setrecursionlimit(x)


def display(f1N, f2N):
    floorID = str(readSpots(5))
    floor1Num = f1N
    floor2Num = f2N
    
    if floorID == str(1):
        floor1Num = str(readSpots(6))

    if floorID == str(2):
        floor2Num = str(readSpots(6))

    platelabel = tk.Label(root, text="Please confirm your license plate: ")
    platelabel.place(relx=0.13, rely=0.1, relwidth=0.75, relheight=0.1)
    
    platef = tk.Frame(root, bg="#99beff", bd=5)
    platef.place(relx=0.5, rely=0.25, relwidth=0.6, relheight=0.1, anchor="n")

    label1 = tk.Label(platef, text="Plate Number: ")
    label1.place(relx=0, rely=0, relwidth=0.45, relheight=1)

    plateNum = readPlate()
    label2 = tk.Label(platef, text=plateNum)
    label2.place(relx=0.55, rely=0, relwidth=0.45, relheight=1)

    spotsLabel = tk.Label(root, text="Availability information: ")
    spotsLabel.place(relx=0.13, rely=0.4, relwidth=0.75, relheight=0.1)
    
    plateframe2 = tk.Frame(root, bg="#99beff", bd=5)
    plateframe2.place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor="n")

    spotInfo = "On Floor " + "1" + " there are " + str(floor1Num) + " spots available"
    label4 = tk.Label(plateframe2, text=spotInfo)
    label4.place(relx=0, rely=0, relwidth=1, relheight=1)

    plateframe3 = tk.Frame(root, bg="#99beff", bd=5)
    plateframe3.place(relx=0.5, rely=0.75, relwidth=0.45, relheight=0.1, anchor="n")

    spotInfo2 = "On Floor " + "2" + " there are " + str(floor2Num) + " spots available"
    label6 = tk.Label(plateframe3, text=spotInfo2)
    label6.place(relx=0, rely=0, relwidth=1, relheight=1)

    root.resizable(False, False)
    root.after(1000, display, floor1Num, floor2Num)

    root.mainloop()


if __name__ == "__main__":
    display(0,0)
