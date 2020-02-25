from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%sx%s" % (width, height))
root.wm_title("Pie Fractions")


def colory():
    val = colorVar.get()
    if val == "1":
        colors = ["#353531", "#ec4e20", "#ff9505", "#016fb9"]
        colorVar.set(options[0])
    elif val == "2":
        colors = ["#52489c", "#f45b69", "#59c3c3", "#4062bb", "#ebebeb"]
        colorVar.set(options[1])
    elif val == "3":
        colors = ["#f4f1de", "#e07a5f", "#3d405b", "#81b29a", "#f2cc8f"]
        colorVar.set(options[2])
    else:
        colors = ["#ac7b84", "#385f71", "#ff5666", "#1affd5", "#cacaaa"]
        colorVar.set(options[3])
    return colors


numBox = Label(root, text="1", font=("Ariel", 40))


def draw(val):
    numBox.configure(text=val)
    pieWidth = int((width / 100))
    pieHeight = int((height / 100))
    colors = colory()
    sizes = []
    labels = []
    numOfFrac = 100 / int(numBox.cget("text"))
    i = 1
    for i in range(int(numBox.cget("text"))):
        sizes.append(numOfFrac)
        labels.append(i + 1)
    fig1, ax1 = plt.subplots(figsize=(pieWidth + 0.5, pieHeight - 2))
    ax1.pie(
        sizes,
        colors=colors,
        labels=labels,
        autopct="%1.2f%%",
        shadow=False,
        startangle=90,
        counterclock=FALSE,
    )
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    canvas = FigureCanvasTkAgg(fig1, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().place(x=(width / 2) - 500, y=(width / 2) - 300)
    canvas.get_tk_widget().place(x=0, y=0)

    def updateSpin():
        print(spin.get())

    spin = Spinbox(root, from_=1, to=2, wrap=TRUE, width=10, command=updateSpin)
    spin.configure(to=int(val))
    spin.place(x=width / 6, y=height - 100)


colorVar = StringVar(root)
options = ["1", "2", "3", "4"]
colorVar.set(options[0])
colorSelector = OptionMenu(root, colorVar, *options, command=colory())
colorSelector.config(width=6)
colorSelector.place(x=1, y=900)
draw(numBox.cget("text"))
slider = Scale(
    root, orient=HORIZONTAL, from_=1, to=24, command=draw, width=25, length=350, show=0,
)
slider.place(x=1100, y=height - 100)
numBox.place(x=1250, y=height - 160)


root.mainloop()

# plt.rcParams["toolbar"] = "None"
