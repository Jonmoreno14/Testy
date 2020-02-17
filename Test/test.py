from tkinter import *
import time
import os

root = Tk()

frames = [PhotoImage(file="fireworksImages/fireworks%i.png" % (i)) for i in range(29)]


def update(ind):

    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    root.after(70, update, ind)


label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()
