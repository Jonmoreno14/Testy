#!/usr/local/bin/python3
from tkinter import *
import random
import Fractions
from pathlib import Path, PureWindowsPath
import ctypes
import os
import time
from tkinter import ttk


def menuWindow():
    menu = Tk()
    # ctypes.windll.shcore.SetProcessDpiAwareness(2)    #uncomment, this is for windows!!!!!!
    ScreenWidth = menu.winfo_screenwidth()
    ScreenHeight = menu.winfo_screenheight()
    menu.geometry("%dx%d+0+0" % (ScreenWidth, ScreenHeight))
    menu.title("Main Menu")
    menu.attributes("-topmost", TRUE)

    # background image
    backgroundImg = PhotoImage(file="Images/87b36abed58b3295ff678aae11e3fb.png")
    background = Label(menu, image=backgroundImg).place(x=0, y=0)

    print(ScreenHeight)
    print(ScreenWidth)

    def openL1():
        menu.destroy()
        lvl1Window()

    def openL2():
        menu.destroy()
        lvl2Window()

    def openL3():
        menu.destroy()
        lvl3Window()

    l1 = Label(menu, text="Fractions", font=("Ariel", 30))
    # l1.config(bg="systemTransparent")
    l1.pack(side=TOP, pady=20)
    b1 = Button(
        menu,
        text="Level 1",
        width=(int((ScreenWidth) / 42)),
        height=(int((ScreenHeight) / 200)),
        font=("Ariel", 32),
        command=openL1,
    )
    b1.pack(side=TOP, pady=20)
    b2 = Button(
        menu,
        text="Level 2",
        width=(int((ScreenWidth) / 42)),
        height=(int((ScreenHeight) / 200)),
        font=("Ariel", 32),
        command=openL1,
    )
    b2.pack(side=TOP, pady=20)

    b3 = Button(
        menu,
        text="Level 3",
        width=(int((ScreenWidth) / 42)),
        height=(int((ScreenHeight) / 200)),
        font=("Ariel", 32),
        command=openL1,
    )
    b3.pack(side=TOP, pady=20)

    try:
        e = Path("Images/SH_box2BSHSUName_021_horizontalstack_3_29.png")
        shsuLogo = PhotoImage(file=e)
    except IOError:
        b = PureWindowsPath(e)
        shsuLogo = PhotoImage(file=b)

    shsuLabel = Label(menu, image=shsuLogo).place(x=20, y=20)

    menu.mainloop()


def lvl1Window():
    lvl1 = Tk()
    ScreenWidth = lvl1.winfo_screenwidth()
    ScreenHeight = lvl1.winfo_screenheight()
    lvl1.geometry("%dx%d+0+0" % (ScreenWidth, ScreenHeight))
    lvl1.attributes("-topmost", TRUE)
    lvl1.title("Fractions")

    # background image
    backgroundImg = PhotoImage(file="Images/87b36abed58b3295ff678aae11e3fb.png")
    background = Label(lvl1, image=backgroundImg).place(x=0, y=0)

    def goBack():
        lvl1.destroy()
        menuWindow()

    try:
        e = Path("Images/eback-button-6-921315_2_15.png")
        bckBtnImage = PhotoImage(file=e)
    except IOError:
        b = PureWindowsPath(1)
        bckBtnImage = PhotoImage(file=b)

    backBtn = Button(
        lvl1, image=bckBtnImage, width=65, height=65, command=goBack,
    ).pack(side=TOP, pady=10, padx=10, anchor=NW)

    numBox = Label(lvl1, text="1", font=("Ariel", 40))

    questionLabel = Label(lvl1, text="1/2", font=("Ariel", 36))

    def show(val):
        numBox.configure(text=val)
        drawFraction(lvl1, questionLabel.cget("text"), numBox.cget("text"))

    def newQuestionFunc():
        randomQuestion = Fractions.level1()
        questionLabel.configure(text=randomQuestion)
        drawFraction(lvl1, questionLabel.cget("text"), numBox.cget("text"))

    slider = Scale(
        lvl1,
        orient=HORIZONTAL,
        from_=1,
        to=18,
        command=show,
        width=25,
        length=(ScreenWidth / 2),
        show=0,
    ).pack(side=BOTTOM, anchor=CENTER, pady=140)

    newQuestionBtn = Button(
        lvl1,
        text="New Question",
        width=(int((ScreenWidth) / 140)),
        height=(int((ScreenHeight) / 290)),
        command=newQuestionFunc,
        font=("Ariel", 14),
    )
    newQuestionBtn.place(
        x=((ScreenWidth / 3)) - (newQuestionBtn.winfo_reqwidth() / 2),
        y=(ScreenHeight / (21 / 18)),
    )

    questionLabel.pack(side=TOP, pady=10)
    numBox.place(
        x=(ScreenWidth / 2) - (numBox.winfo_reqwidth() / 2), y=(ScreenHeight / 4) * 3
    )

    drawFraction(
        lvl1, questionLabel.cget("text"), numBox.cget("text"),
    )

    lvl1.mainloop()


def lvl2Window():
    pass


def lvl3Window():
    pass


def drawFraction(windowName, question, sliderFraction):
    ScreenWidth = windowName.winfo_screenwidth()
    ScreenHeight = windowName.winfo_screenheight()
    currFraction = question.split("/")  # took string split into array
    numerator = int(currFraction[0])  # turning the str numer. to int
    denominator = int(currFraction[1])  # same as ^ but denom.
    sliderFraction = int(sliderFraction)
    canWidth = ScreenWidth / 2
    canHeight = (ScreenHeight / 100) * 48  # 540
    canvas = Canvas(
        windowName,
        bg="gray",
        width=canWidth,
        height=canHeight,
        highlightbackground="black",
    )
    canvas.place(
        x=(ScreenWidth / 2) - (canvas.winfo_reqwidth() / 2), y=(ScreenHeight / 6),
    )

    options = ["Blue", "Green", "Red", "Yellow"]
    colorVar = StringVar(windowName)
    colorVar.set(options[0])
    colorSelector = OptionMenu(windowName, colorVar, *options)
    colorSelector.config(width=15)
    colorSelector.place(x=ScreenWidth / 70, y=ScreenHeight / 3)
    colorSelectorLabel = Label(
        windowName, text="Color Selector:", font=("Ariel", 14)
    ).place(
        x=(ScreenWidth / 70) + (colorSelector.winfo_reqwidth() / (14 / 3)),
        y=ScreenHeight / (10 / 3),
    )

    x = 1
    j = 1
    n = canWidth / sliderFraction
    l = canWidth / denominator
    for j in range(numerator):
        rec = canvas.create_rectangle(
            (l * x),
            (0),
            (canWidth / denominator) * j,
            canHeight + 10,
            fill=str(colorVar.get()),
        )

    for x in range(denominator):
        canvas.create_line((l * x), 0, (l * x), 1000, width=3, dash=(14, 18))
        END

    for x in range(sliderFraction):
        canvas.create_line((n * x), 0, (n * x), 1000, width=3, fill="Black")
        END

    def checkAnswerFunc():
        if sliderFraction % denominator == 0:
            print("Correct")
            FireworkAnimation()
        else:
            print("Wrong")

    checkAnswerBtn = Button(
        windowName,
        text="Check Answer",
        width=(int((ScreenWidth) / 140)),
        height=(int((ScreenHeight) / 290)),
        font=("Ariel", 14),
        command=checkAnswerFunc,
    )
    checkAnswerBtn.place(
        x=((ScreenWidth / 3) * 2) - (checkAnswerBtn.winfo_reqwidth()),
        y=(ScreenHeight / (21 / 18)),
    )

    def FireworkAnimation():
        frames = [
            PhotoImage(file="fireworksImages/fireworks%i.png" % (i)) for i in range(29)
        ]

        def update(ind):
            frame = frames[ind]
            ind += 1
            gif.configure(image=frame)
            # make gif transparent background, for MAC ONLY!, comment the line below
            gif.config(bg="systemTransparent")
            # gif.wm_attributes("-transparentcolor", "white") # for WINDOWS!
            windowName.after(70, update, ind)

        gif = Label(windowName)
        gif.place(x=1010, y=890)
        windowName.after(0, update, 0)
        windowName.mainloop()


menuWindow()
