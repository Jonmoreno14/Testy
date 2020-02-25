#!/usr/local/bin/python3
from tkinter import *
import random
import Fractions
from pathlib import Path, PureWindowsPath
import ctypes
import os
import time
from tkinter import ttk
from PIL import ImageTk, Image


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
        drawFraction(numBox.cget("text"), questionLabel.cget("text"))

    def newQuestionFunc():
        randomQuestion = Fractions.level1()
        questionLabel.configure(text=randomQuestion)
        drawFraction(numBox.cget("text"), questionLabel.cget("text"))

    slider = Scale(
        lvl1,
        orient=HORIZONTAL,
        from_=1,
        to=12,
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

    options = ["Blue", "Green", "Red", "Yellow"]
    colorVar = StringVar(lvl1)
    colorVar.set(options[0])
    colorSelector = OptionMenu(lvl1, colorVar, *options)
    colorSelector.config(width=15)
    colorSelector.place(x=ScreenWidth / 70, y=ScreenHeight / 3)
    colorSelectorLabel = Label(lvl1, text="Color Selector:", font=("Ariel", 14)).place(
        x=(ScreenWidth / 70) + (colorSelector.winfo_reqwidth() / (14 / 3)),
        y=ScreenHeight / (10 / 3),
    )

    def drawFraction(val, question):
        currFraction = question.split("/")  # took string split into array
        numerator = int(currFraction[0])  # turning the str numer. to int
        denominator = int(currFraction[1])  # same as ^ but denom.
        sliderFraction = int(val)
        canWidth = ScreenWidth / 2
        canHeight = (ScreenHeight / 100) * 48  # 540
        canvas = Canvas(
            lvl1,
            bg="gray",
            width=canWidth,
            height=canHeight,
            highlightbackground="black",
        )
        canvas.place(
            x=(ScreenWidth / 2) - (canvas.winfo_reqwidth() / 2), y=(ScreenHeight / 6),
        )

        x = 1
        n = canWidth / sliderFraction
        l = canWidth / denominator

        rec = canvas.create_rectangle(
            0,
            0,
            (canWidth / denominator) * numerator,
            canHeight + 10,
            fill=str(colorVar.get()),
        )
        lvl1.update_idletasks

        for x in range(denominator):
            canvas.create_line((l * x), 0, (l * x), 1000, width=3, dash=(14, 18))
            END

        for x in range(sliderFraction):
            canvas.create_line((n * x), 0, (n * x), 1000, width=3, fill="Black")
            END

        def checkAnswerFunc():
            if sliderFraction % denominator == 0:
                equivNumerator = sliderFraction / denominator
                equivFrac = int(equivNumerator) * numerator
                string = "%i/%i" % (equivFrac, sliderFraction)
                correctLabel = Label(
                    lvl1,
                    text="Correct! %s is equvilent to %s" % (question, string),
                    font=("Ariel", 20),
                )
                correctLabel.place(
                    x=(ScreenWidth / 2) - (correctLabel.winfo_reqwidth() / 2),
                    y=(ScreenHeight / 3) * 2,
                )
                FireworkAnimation()
            else:
                print("Wrong")

        checkAnswerBtn = Button(
            lvl1,
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
            frameImagesPath = "fireworksImages"
            spriteSheetPath = "fireworks"
            imageType = ".png"
            myImg = PhotoImage(
                file=frameImagesPath + "/" + spriteSheetPath + str(0) + imageType
            )
            initX = canvas.winfo_width() / 2 - myImg.width() / 2
            initX4 = initX3 = initX2 = initX1 = initX
            initY = canvas.winfo_height() - myImg.height() / 4
            initY4 = initY3 = initY2 = initY1 = initY
            animationHold = 0
            for i in range(29):
                myImg = PhotoImage(
                    file=frameImagesPath + "/" + spriteSheetPath + str(i) + imageType
                )
                canvas.create_image(initX, initY, image=myImg, anchor=NW)
                canvas.create_image(initX1, initY1, image=myImg, anchor=NW)
                canvas.create_image(initX2, initY2, image=myImg, anchor=NW)
                canvas.create_image(initX3, initY3, image=myImg, anchor=NW)
                canvas.create_image(initX4, initY4, image=myImg, anchor=NW)
                initY = initY - 14
                initY1 = initY1 - 12
                initY2 = initY2 - 12
                initY3 = initY3 - 7
                initY4 = initY4 - 7
                initX1 = initX1 - 6
                initX2 = initX2 + 6
                initX3 = initX3 - 12
                initX4 = initX4 + 12
                lvl1.update()
                time.sleep(0.3 / 10)

        # def WrongAnswerAnimation():

    drawFraction(numBox.cget("text"), questionLabel.cget("text"))
    lvl1.mainloop()


def lvl2Window():
    pass


def lvl3Window():
    pass


menuWindow()
