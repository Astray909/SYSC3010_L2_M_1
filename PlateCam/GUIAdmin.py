from Tkinter import *
import datetime
import sys
import os

from TS_Download import *
from TS_Update import *
import Tkinter as tk

#set the default size for GUI window
HEIGHT = 500
WIDTH = 600

#initialize GUI canvas
root = tk.Tk()
root.title("GUI - For Admins")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

def openGate():
    print("wrote YES to field 3, gate will now open")
    writeTS("Gate Open Override", "", "YES") #writes to thingspeak, signaling gate to open

def closeGate():
    print("wrote NO to field 3, gate will now close")
    writeTS("Gate Close Override", "", "NO") #writes to thingspeak, signaling gate to close
    time.sleep(5)
    writeTS("Gate Close Override", "", "00")

def camOn():
    print("wrote A1 to field3, camera will now turn on")
    writeTS("Camera Override", "", "B1") #writes to thingspeak, signaling camera to turn on

def display():
    
    platelabel = tk.Label(root, text="Please choose from the following options: ")
    platelabel.place(relx=0.13, rely=0.1, relwidth=0.75, relheight=0.1)

    #contains 3 frames, and each frame contains a button
    openframe = tk.Frame(root, bg="#a3881a", bd=5)
    openframe.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.2, anchor="n")

    openbutton = tk.Button(
        openframe, text="Open Gate", font=40, fg="black", command=openGate
    )
    openbutton.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

    closeframe = tk.Frame(root, bg="#a3881a", bd=5)
    closeframe.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.2, anchor="n")

    closebutton = tk.Button(
        closeframe, text="Close Gate", font=40, fg="black", command=closeGate
    )
    closebutton.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

    camframe = tk.Frame(root, bg="#a3881a", bd=5)
    camframe.place(relx=0.5, rely=0.75, relwidth=0.5, relheight=0.2, anchor="n")

    cambutton = tk.Button(
        camframe, text="Turn on Camera", font=40, fg="black", command=camOn
    )
    cambutton.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

    #set GUI to be non resizable
    root.resizable(False, False)

    root.mainloop()


if __name__ == "__main__":
    display() #start GUI
