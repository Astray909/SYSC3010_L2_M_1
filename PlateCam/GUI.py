from Tkinter import *
import datetime

from TS_Download import *
import Tkinter as tk

HEIGHT = 500
WIDTH = 900

root = tk.Tk()
root.title("GUI")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


def display():

    platelabel = tk.Label(root, text="Please confirm your license plate: ")
    platelabel.place(relx=0.13, rely=0.1, relwidth=0.75, relheight=0.1)
    
    platef = tk.Frame(root, bg="#ff99cc", bd=5)
    platef.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor="n")

    label1 = tk.Label(platef, text="Plate Number: ")
    label1.place(relx=0, rely=0, relwidth=0.45, relheight=1)

    label2 = tk.Label(platef, text=readPlate())
    label2.place(relx=0.5, rely=0, relwidth=0.45, relheight=1)

    plateframe2 = tk.Frame(root, bg="#ff99cc", bd=5)
    plateframe2.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor="n")

    label3 = tk.Label(plateframe2, text="Available Parking Information: ")
    label3.place(relx=0, rely=0, relwidth=0.45, relheight=1)

    spotInfo = "There are " + readSpots(5) + " floors and " + readSpots(6) + " spots available"
    label4 = tk.Label(plateframe2, text=spotInfo)
    label4.place(relx=0.5, rely=0, relwidth=0.45, relheight=1)

    root.resizable(False, False)
    root.after(1000, display)

    root.mainloop()


if __name__ == "__main__":
    display()
