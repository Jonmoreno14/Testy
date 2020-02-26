from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import random
import numpy as np


lvlFrac = Tk()
width = lvlFrac.winfo_screenwidth()
height = lvlFrac.winfo_screenheight()
lvlFrac.geometry("%sx%s" % (width, height))
lvlFrac.wm_title("Pie Fractions")


def colory():
    val = colorVar.get()
    if val == "color way 1":
        colors = ["#595959", "#ec4e20", "#ff9505", "#016fb9"]
        colorVar.set(colorOptions[0])
    elif val == "color way 2":
        colors = ["#52489c", "#f45b69", "#59c3c3", "#4062bb", "#ebebeb"]
        colorVar.set(colorOptions[1])
    elif val == "color way 3":
        colors = ["#f4f1de", "#e07a5f", "#3d405b", "#81b29a", "#f2cc8f"]
        colorVar.set(colorOptions[2])
    else:
        colors = ["#ac7b84", "#385f71", "#ff5666", "#1affd5", "#cacaaa"]
        colorVar.set(colorOptions[3])
    return colors


numBox = Label(lvlFrac, text="1", font=("Ariel", 40))


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
    fig1, ax1 = plt.subplots(
        linewidth=10, edgecolor="#04235a", figsize=(pieWidth + 0.5, pieHeight - 2)
    )
    # remove these 2 lines
    fig1.set_figwidth(8)
    fig1.set_figheight(8)

    fig1.subplots_adjust(left=0, right=1, bottom=0.1, top=0.9)
    ax1.pie(
        sizes,
        colors=colors,
        labels=labels,
        autopct="%1.2f%%",
        shadow=False,
        startangle=90,
        counterclock=FALSE,
    )
    plt.rcParams["font.size"] = 14

    fig1.set_facecolor("#e6e6e6")
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    canvas = FigureCanvasTkAgg(fig1, master=lvlFrac)  # A tk.DrawingArea.
    canvas.draw()
    # canvas.get_tk_widget().place(x=(width / 2) - 500, y=(width / 2) - 300)
    canvas.get_tk_widget().place(x=(width / 2) - 400, y=(height / 2) - 500)


colorVar = StringVar(lvlFrac)
colorOptions = ["color way 1", "color way 2", "color way 3", "color way 4"]
colorVar.set(colorOptions[0])
colorSelector = OptionMenu(lvlFrac, colorVar, *colorOptions, command=colory())
colorSelector.config(width=10)
colorSelector.place(x=1, y=900)

draw(numBox.cget("text"))
slider = Scale(
    lvlFrac,
    orient=HORIZONTAL,
    from_=1,
    to=24,
    command=draw,
    width=25,
    length=650,
    show=0,
)
slider.place(x=(width / 2) - slider.winfo_reqwidth() / 2, y=height - 100)
numBox.place(x=width / 2, y=height - 160)


lvlFrac.mainloop()
