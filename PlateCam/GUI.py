from Tkinter import *
import datetime

from TS_Download import *
import Tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title("GUI")
canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH )
canvas.pack()

def display():

    platelabel = tk.Label(root, text = "Please confirm your license plate: ")
    platelabel.place(relx = 0.13, rely =0.1, relwidth = 0.75, relheight = 0.1)

    platef = tk.Frame(root,bg = '#ff99cc',bd = 5)
    platef.place(relx = 0.5, rely = 0.25,relwidth = 0.75, relheight = 0.1,anchor = 'n')

    label1 = tk.Label(platef, text = "Plate Number: ")
    label1.place(relx = 0, rely =0, relwidth = 0.3, relheight = 1)

    label2 = tk.Label(platef,text = readPlate())
    label2.place(relx = 0.35, rely = 0,relwidth = 0.65, relheight = 1)

    plateframe2 = tk.Frame(root,bg = '#ff99cc',bd = 5)
    plateframe2.place(relx = 0.5, rely = 0.5,relwidth = 0.15, relheight = 0.1,anchor = 'n')

    changeframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
    changeframe.place(relx = 0.5, rely = 0.35,relwidth = 0.75, relheight = 0.1,anchor = 'n')

    label2 = tk.Label(changeframe, text = "Number correction: ")
    label2.place(relx = 0, rely =0, relwidth = 0.3, relheight = 1)

    entry2 = tk.Entry(changeframe,font = 40)
    entry2.place(relx = 0.35, rely = 0,relwidth = 0.65, relheight = 1)

    refreshbutton = tk.Button(plateframe2,text = "Refresh",font = 40,  fg =  'black')
    refreshbutton.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')

    root.resizable(False, False)
    root.after(1000, display)

    root.mainloop()

if __name__ == "__main__":
    display()