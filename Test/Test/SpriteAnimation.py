from tkinter import *
from PIL import Image, ImageTk
import time


def FireworkAnimation():
    # CUSTOMIZATION
    columns = 6
    rows = 5
    framesPerSecond = 10
    imageType = ".png"  # image type
    spriteSheetPath = "fireworks"  # minus image type
    frameImagesPath = "fireworksImages"  # frame save folder path
    backgroundColor = "black"

    # automatically adjusted variables
    im = Image.open(spriteSheetPath + imageType)
    ssWidth, ssHeight = im.size
    print("width", ssWidth, "height", ssHeight)
    frameWidth = ssWidth // columns
    frameHeight = ssHeight // rows
    frameImagesPath = frameImagesPath + "/" + spriteSheetPath

    root = Tk()
    canvas = Canvas(root, width=frameWidth, height=frameHeight, bg=backgroundColor)
    canvas.pack()

    # frame coordinates top left x,y = 0
    unitRight = ssWidth // columns
    unitBottom = ssHeight // rows
    unitLeft = 0
    unitTop = 0

    # splits images in sprite sheet
    def crop(filename, newname):
        im = Image.open(spriteSheetPath + imageType)
        im1 = im.crop((unitLeft, unitTop, unitRight, unitBottom))
        im1.save(newname)

    # saves split images into a file
    frameCount = 0
    for i in range(rows):
        for j in range(columns):
            newPath = frameImagesPath + str(frameCount) + imageType
            crop(spriteSheetPath + imageType, newPath)
            unitLeft = unitLeft + ssWidth // columns
            unitRight = unitRight + ssWidth // columns
            frameCount = frameCount + 1
            print(unitLeft, ",", unitTop, "&", unitRight, ",", unitBottom)
        unitLeft = 0
        unitRight = ssWidth // columns
        unitTop = unitTop + ssHeight // rows
        unitBottom = unitBottom + ssHeight // rows

    # animation loop
    for x in range(rows * columns):
        myImg = PhotoImage(file=frameImagesPath + str(x) + imageType)
        canvas.create_image(20, 20, image=myImg, anchor=NW)
        root.update()
        time.sleep(0.6 / framesPerSecond)


FireworkAnimation()
