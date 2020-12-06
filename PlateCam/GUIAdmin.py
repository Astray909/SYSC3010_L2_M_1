from Tkinter import *
import datetime
import sys
import os

from TS_Download import *
from TS_Update import *
import Tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title("GUI - For Admins")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

def openGate():
    print("wrote YES to field 3, gate will now open")
    writeTS("", "", "YES")

def closeGate():
    print("wrote NO to field 3, gate will now close")
    writeTS("", "", "NO")

def display():

    platelabel = tk.Label(root, text="Please choose from the following options: ")
    platelabel.place(relx=0.13, rely=0.1, relwidth=0.75, relheight=0.1)

    openframe = tk.Frame(root, bg="#ff99cc", bd=5)
    openframe.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.2, anchor="n")

    openbutton = tk.Button(
        openframe, text="Open Gate", font=40, fg="black", command=openGate
    )
    openbutton.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

    closeframe = tk.Frame(root, bg="#ff99cc", bd=5)
    closeframe.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.2, anchor="n")

    closebutton = tk.Button(
        closeframe, text="Close Gate", font=40, fg="black", command=closeGate
    )
    closebutton.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

    root.resizable(False, False)

    root.mainloop()


if __name__ == "__main__":
    display()
