#!/usr/local/bin/python3
from kivy.app import App
from kivy.lang import Builder
import os
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.graphics import Rectangle, Color, Line
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from subprocess import call
import teacherGradeViewer
import Fractions
import random
import sqlite3
import hashlib
Window.clearcolor = (1, 1, 1, 1)
Window.size = (1200, 800)

conn = sqlite3.connect("UserInfo.db")
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS login(user TEXT NOT NULL, password TEXT);")

Fl = FloatLayout()


def FractionEq(self):
    def goBack(self):
        Fl.clear_widgets()
        GameSelector(self)

    def update_rect(*args):
        width = Fl.size[0] / 5 * 3
        height = Fl.size[1] / 5 * 3
        rec.pos = ((Fl.width / 5), (Fl.height * (3 / 11)))
        rec.size = (width, height)

    def update_line(*args):
        width = Fl.size[0] / 5 * 3
        height = Fl.size[1] / 5 * 3
        for x in range(1, denominator):
            line.points = [((width/denominator) * x) + Fl.size[0] / 5, (Fl.height * (13 / 15)),
                           ((width/denominator) * x) + Fl.size[0] / 5, (Fl.height * (5 / 18))]
            line.dash_length = 60
            line.dash_offset = 60

    def update_numerator(*args):
        width = ((Fl.size[0] / 5 * 3) / denominator) * numerator
        height = Fl.size[1] / 5 * 3
        line.dash_length = 60
        line.dash_offset = 60
        rec2.pos = ((Fl.width / 5), (Fl.height * (3 / 11)))
        rec2.size = (width, height)

    def sliderValFunc(instance, val):
        sliderVal.text = "%d" % val

    def newQuestionFunc(self):
        randomQuestion = Fractions.level1()
        questionLabel.text = randomQuestion
        currFraction = questionLabel.text.split("/")
        denominator = int(currFraction[1])
        Fl.clear_widgets()
        FractionEq(self)

    wid = Widget()
    wid1 = Widget()
    wid2 = Widget()

    logo = Image(
        source='/Users/jonathonmoreno/Desktop/SE/Test/Images/SH_box2BSHSUName_021_horizontalstack_3_29.png',
        allow_stretch=True,
        pos_hint={"x": .01, 'y': .9},
        size_hint=(.2, .1))

    backBtnImage = Image(
        source='/Users/jonathonmoreno/Desktop/SE/Test/Images/eback-button-6-921315_2_15.png',
        pos_hint={"x": .01, 'y': .83},
        size_hint=(.04, .07),
        keep_ratio=True)

    backBtn = Button(pos_hint={"x": .01, 'y': .83},
                     size_hint=(.141, .07),
                     background_color=(1, 1, 1, .01))
    backBtn.bind(on_release=goBack)

    questionLabel = Label(text=Fractions.level1(),
                          font_size=68,
                          color=(.1, .1, .1, 1),
                          pos_hint={'x': .5, 'y': .93},
                          size_hint=(.001, .001))

    slider = Slider(min=1,
                    max=28,
                    step=1,
                    pos_hint={'x': .2, 'y': .15},
                    size_hint=(.6, .05))
    slider.bind(value=sliderValFunc)

    sliderVal = Label(text='1',
                      font_size=68,
                      color=(.1, .1, .1, 1),
                      pos_hint={'x': .5, 'y': .22},
                      size_hint=(.001, .001))

    newQuestionBtn = Button(text='New Question',
                            size_hint=(.1, .08),
                            pos_hint={'x': .25, 'y': .05})
    newQuestionBtn.bind(on_release=newQuestionFunc)

    checkAnswerBtn = Button(text='Check Answer',
                            size_hint=(.1, .08),
                            pos_hint={'x': .65, 'y': .05})

    currFraction = questionLabel.text.split("/")
    numerator = int(currFraction[0])
    denominator = int(currFraction[1])

    width = Fl.size[0] / 5 * 3
    height = Fl.size[1] / 5 * 3

    with wid.canvas:
        Color(.9, .9, .9)
        rec = Rectangle(size=(width, height),
                        pos=((Fl.width / 2) - (Fl.width / 4),
                             (Fl.height / 2) - (Fl.height / 4)))

    wid.bind(pos=update_rect)
    wid.bind(size=update_rect)

    with wid1.canvas:
        Color(.1, .1, .1)
        for x in range(1, denominator):
            line = Line(points=[(((width/denominator) * x) + Fl.size[0] / 5), (Fl.height * (13 / 15)),
                                (((width/denominator) * x) + Fl.size[0] / 5), (Fl.height * (5 / 18))],
                        dash_length=60, dash_offset=60, width=1, color=(.23, .6, .2))

    wid1.bind(pos=update_line)
    wid1.bind(size=update_line)

    with wid2.canvas:
        Color(.3, .3, .6)
        rec2 = Rectangle(size=((width / denominator)*numerator, height),
                         pos=((Fl.width / 2) - (Fl.width / 3),
                              (Fl.height / 2) - (Fl.height / 4)))

    wid2.bind(pos=update_numerator)
    wid2.bind(size=update_numerator)

    Fl.add_widget(logo)
    Fl.add_widget(backBtnImage)
    Fl.add_widget(backBtn)
    Fl.add_widget(slider)
    Fl.add_widget(questionLabel)
    Fl.add_widget(sliderVal)
    Fl.add_widget(newQuestionBtn)
    Fl.add_widget(checkAnswerBtn)
    Fl.add_widget(wid)
    Fl.add_widget(wid1)
    Fl.add_widget(wid2)


def PieFraction(self):
    def draw():
        pass

    def goBack(self):
        Fl.clear_widgets()
        GameSelector(self)

    logo = Image(
        source='/Users/jonathonmoreno/Desktop/SE/Test/Images/SH_box2BSHSUName_021_horizontalstack_3_29.png',
        allow_stretch=True,
        pos_hint={'x': .01, 'y': .9},
        size_hint=(.2, .1))

    backBtnImage = Image(
        source='/Users/jonathonmoreno/Desktop/SE/Test/Images/eback-button-6-921315_2_15.png',
        pos_hint={'x': .01, 'y': .83},
        size_hint=(.04, .07),
        keep_ratio=True)

    backBtn = Button(pos_hint={"x": .01, 'y': .83},
                     size_hint=(.141, .07),
                     background_color=(1, 1, 1, .01))
    backBtn.bind(on_release=goBack)

    Fl.add_widget(logo)
    Fl.add_widget(backBtnImage)
    Fl.add_widget(backBtn)


def GameSelector(self):
    def goBack(self):
        Fl.clear_widgets()
        MainWindow(self)

    def goFrac(self):
        Fl.clear_widgets()
        FractionEq(self)

    def goPie(self):
        Fl.clear_widgets()
        PieFraction(self)

    Fl.clear_widgets()

    logo = Image(
        source='/Users/jonathonmoreno/Desktop/SE/Test/Images/SH_box2BSHSUName_021_horizontalstack_3_29.png',
        allow_stretch=True,
        pos_hint={"x": .01, 'y': .9},
        size_hint=(.2, .1))
    fractionEq = Button(text='Fraction Equivilence',
                        pos_hint={"x": .3, 'y': .6},
                        font_size=46,
                        size_hint=(.4, .25),
                        color=(0, 0, 0, 1),
                        background_color=(1, 1, 1, .6))
    fractionEq.bind(on_release=goFrac)

    pieFraction = Button(text='Pie Fractions',
                         pos_hint={"x": .3, 'y': .2},
                         font_size=46,
                         size_hint=(.4, .25),
                         color=(0, 0, 0, 1),
                         background_color=(1, 1, 1, .6))
    pieFraction.bind(on_release=goPie)

    backBtnImage = Image(
        source='/Users/jonathonmoreno/Desktop/SE/Test/Images/eback-button-6-921315_2_15.png',
        pos_hint={"x": .01, 'y': .83},
        size_hint=(.04, .07),
        keep_ratio=True)

    backBtn = Button(pos_hint={"x": .01, 'y': .83},
                     size_hint=(.141, .07),
                     background_color=(1, 1, 1, .01))
    backBtn.bind(on_release=goBack)

    Fl.add_widget(logo)
    Fl.add_widget(fractionEq)
    Fl.add_widget(pieFraction)
    Fl.add_widget(backBtnImage)
    Fl.add_widget(backBtn)


def MainWindow(self):
    def teacherFunc(self):
        def submitFunc2(self):
            encrypted = hashlib.md5(str(
                passInput.text).encode("utf-8")).hexdigest()
            sql = "SELECT * FROM login WHERE user = '" + str(
                userInput.text) + "' AND password = '" + encrypted + "'"
            cursor.execute(sql)
            conn.commit()
            if cursor.fetchone() is not None:
                print("Welcome")
                Fl.clear_widgets()
                # App.get_running_app().stop()
                #call(["python", "rip.py"])
                #os.system('python rip.py')
                teacherGradeViewer.runApp()
            else:
                wrong = Label(text='Incorrect password!',
                              color=(1, 0, 0, 1),
                              pos_hint={"x": .4, 'y': .25},
                              font_size=36,
                              size_hint=(.2, .1))
                Fl.add_widget(wrong)

        Fl.remove_widget(submitBtn)
        passLabel = Label(text='Enter your password:',
                          color=(0, 0, 0, 1),
                          pos_hint={"x": .01, 'y': .35},
                          font_size=46,
                          size_hint=(.2, .1))

        passInput = TextInput(multiline=False,
                              pos_hint={"x": .3, 'y': .36},
                              font_size=46,
                              size_hint=(.4, .07),
                              password=True,
                              cursor_blink=True,
                              write_tab=False)

        submitBtn2 = Button(text="Submit",
                            pos_hint={"x": .38, 'y': .03},
                            size_hint=(.25, .15),
                            color=(0, 0, 0, 1),
                            background_color=(1, 1, 1, .6))
        submitBtn2.bind(on_release=submitFunc2)

        Fl.add_widget(passLabel)
        Fl.add_widget(passInput)
        Fl.add_widget(submitBtn2)

    def submitFunc(self):
        if str(userInput.text) == "":
            errorMessage = Label(text="Enter a name!",
                                 color=(1, 0, 0, 1),
                                 pos_hint={"x": .4, 'y': .25},
                                 font_size=36,
                                 size_hint=(.2, .1))
            Fl.add_widget(errorMessage)
        else:
            try:
                sql = "INSERT INTO login(user,password) VALUES('" + str(
                    userInput.text) + "',NULL)"
                cursor.execute(sql)
                conn.commit()
                print("User " + str(userInput.text) + " was created!")
                GameSelector(self)
            except:
                student = str(userInput.text)
                print(student)
                GameSelector(self)

    logo = Image(
        source='/Users/jonathonmoreno/Desktop/SE/Test/Images/SH_box2BSHSUName_021_horizontalstack_3_29.png',
        allow_stretch=True,
        pos_hint={"x": .01, 'y': .9},
        size_hint=(.2, .1))

    userLabel = Label(text='Enter your name:',
                      color=(0, 0, 0, 1),
                      pos_hint={"x": .026, 'y': .59},
                      font_size=46,
                      size_hint=(.2, .1))

    userInput = TextInput(multiline=False,
                          pos_hint={"x": .30, 'y': .6},
                          font_size=46,
                          size_hint=(.4, .07),
                          cursor_blink=True,
                          write_tab=False)

    submitBtn = Button(text="Submit",
                       pos_hint={"x": .38, 'y': .03},
                       size_hint=(.25, .15),
                       color=(0, 0, 0, 1),
                       background_color=(1, 1, 1, .6))
    submitBtn.bind(on_release=submitFunc)

    teacherHead = Image(
        source='/Users/jonathonmoreno/Desktop/SE/Test/Images/account.png',
        pos_hint={"x": .9, 'y': .03},
        size_hint=(.04, .07),
        keep_ratio=True)

    teacherHeadBtn = Button(pos_hint={"x": .80, 'y': .03},
                            size_hint=(.141, .07),
                            background_color=(1, 1, 1, .01))
    teacherHeadBtn.bind(on_release=teacherFunc)

    teacherLabel = Label(text="Teacher Login",
                         color=(0, 0, 0, 1),
                         pos_hint={"x": .75, 'y': .018},
                         font_size=30,
                         size_hint=(.2, .1))

    Fl.add_widget(userLabel)
    Fl.add_widget(logo)
    Fl.add_widget(userInput)
    Fl.add_widget(submitBtn)
    Fl.add_widget(teacherHeadBtn)
    Fl.add_widget(teacherHead)
    Fl.add_widget(teacherLabel)


class MyMainApp(App):
    def build(self):
        MainWindow(self)
        self.title = 'Fractions'
        return Fl


if __name__ == "__main__":
    MyMainApp().run()
