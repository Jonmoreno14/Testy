# TODO on correct answer the feedback text (example: 1/6 is equal to 1/6)
#    doesn't adjust to screen size and covers up "new question" and "check answer"
#    buttons
# TODO add fireworks animation
# TODO pie chart could be adjusted to fit better to screen
# TODO optional, back button to menu

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
from kivy.graphics import Rectangle, Color, Line, Ellipse
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
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
    "CREATE TABLE IF NOT EXISTS login(user TEXT NOT NULL, password TEXT, incorrect TEXT);")

Fl = FloatLayout()
wid3 = Widget()

# load sounds
rightSound = SoundLoader.load('Audio/success.ogg')
wrongSound = SoundLoader.load('Audio/wrong.ogg')
studentName = ""


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

    def update_sliderNum(*args):
        width = Fl.size[0] / 5 * 3
        height = Fl.size[1] / 5 * 3
        for x in range(1, slider.value):
            line2.points = [((width/slider.value) * x) + Fl.size[0] / 5, (Fl.height * (13 / 15)),
                            ((width/slider.value) * x) + Fl.size[0] / 5, (Fl.height * (5 / 18))]

    def sliderLines():
        with wid3.canvas:
            wid3.canvas.clear()
            Color(.1, .1, .1)
            for x in range(1, slider.value):
                line2 = Line(points=[(((width/slider.value) * x) + Fl.size[0] / 5), (Fl.height * (13 / 15)),
                                     (((width/slider.value) * x) + Fl.size[0] / 5), (Fl.height * (5 / 18))],
                             width=4, color=(.23, .6, .2))

        # wid3.bind(pos=update_sliderNum)
        # wid3.bind(size=update_sliderNum)
        Fl.add_widget(wid3)

    def sliderValFunc(instance, val):
        sliderVal.text = "%d" % val
        Fl.remove_widget(wid3)
        sliderLines()
        return sliderVal.text

    def newQuestionFunc(self):
        randomQuestion = Fractions.level1()
        questionLabel.text = randomQuestion
        currFraction = questionLabel.text.split("/")
        denominator = int(currFraction[1])
        Fl.clear_widgets()
        FractionEq(self)

    def answerChecker(self):
        if int(slider.value) % denominator == 0:
            equivNumerator = int(slider.value) / denominator
            equiviFrac = int(equivNumerator) * numerator
            newFrac = "%i/%i" % (equiviFrac, slider.value)
            response = "%i/%i" % (equiviFrac, int(slider.value))
            checkAnswerBtn.background_normal = ''
            checkAnswerBtn.background_color = (.1, .7, .2, .9)
            rightSound.play()
            rightResponse = TimedRightResponse()
            correctResp = Label(text='%s is equal to %s' % (str(questionLabel.text), str(newFrac)),
                                color=(0, 0, 0, 1),
                                font_size=62,
                                pos_hint={"x": .4, 'y': .06},
                                size_hint=(.2, .1))
            Fl.add_widget(correctResp)
        else:
            wrongSound.play()
            checkAnswerBtn.background_normal = ('')
            checkAnswerBtn.background_color = (1, .3, .3, .9)
            checkAnswerBtn.text = ("TRY AGAIN")
            # UPDATE categories SET code = CONCAT(code, '_standard') WHERE id = 1;
            try:
                sql = "UPDATE login SET incorrect = incorrect || ' "+str(
                    slider.value)+str("/")+str(denominator)+",' WHERE user = '"+studentName+"';"
                # sql = "UPDATE login SET incorrect = incorrect || '"+str(
                #   slider.value)+str("/")+str(denominator)+"' WHERE user = "+studentName+"; "
                cursor.execute(sql)
                conn.commit()
                print(sql)
            except:
                sql = "UPDATE login SET incorrect = incorrect || '"+str(
                    slider.value)+str("/")+str(denominator)+"' WHERE user = "+studentName+"; "
                print(sql)
                print("Failed to add inc. ans")

            wrongResponse = TimedWrongResponse()
            '''incorrectResp = Label(text='Wrong!',
                                  color=(0, 0, 0, 1),
                                  font_size=62,
                                  pos_hint={"x": .4, 'y': .06},
                                  size_hint=(.2, .1))
            Fl.add_widget(incorrectResp)'''

    class TimedRightResponse(Widget):
        myCount = 0
        boolRun = True

        def __init__(self, **kwargs):
            Clock.schedule_interval(self.update, 1)
            super(TimedRightResponse, self).__init__(**kwargs)

        def update(self, *args):
            if self.boolRun == True:
                if self.myCount < 1:
                    print(self.myCount)
                    self.myCount += 1
                else:
                    checkAnswerBtn.background_color = (.4, .4, .4, 1)
                    checkAnswerBtn.text = 'Check Answer'
                    self.myCount = 0
                    self.boolRun = False

    class TimedWrongResponse(Widget):
        myCount = 0
        boolRun = True

        def __init__(self, **kwargs):
            Clock.schedule_interval(self.update, 1)
            super(TimedWrongResponse, self).__init__(**kwargs)

        def update(self, *args):
            if self.boolRun == True:
                if self.myCount < 1:
                    print(self.myCount)
                    self.myCount += 1
                else:
                    checkAnswerBtn.background_color = (.4, .4, .4, 1)
                    checkAnswerBtn.text = 'Check Answer'
                    self.myCount = 0
                    self.boolRun = False

    wid = Widget()
    wid1 = Widget()
    wid2 = Widget()

    logo = Image(
        source='Images/SH_box2BSHSUName_021_horizontalstack_3_29.png',
        allow_stretch=True,
        pos_hint={"x": .01, 'y': .9},
        size_hint=(.2, .1))

    backBtnImage = Image(
        source='Images/eback-button-6-921315_2_15.png',
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
                            # background_color = (1,1,1,1),
                            size_hint=(.1, .08),
                            pos_hint={'x': .65, 'y': .05})
    checkAnswerBtn.bind(on_release=answerChecker)

    currFraction = questionLabel.text.split("/")
    numerator = int(currFraction[0])
    denominator = int(currFraction[1])

    width = Fl.size[0] / 5 * 3
    height = Fl.size[1] / 5 * 3

    # draws blank canvas
    with wid.canvas:
        Color(.9, .9, .9)
        rec = Rectangle(size=(width, height),
                        pos=((Fl.width / 2) - (Fl.width / 4),
                             (Fl.height / 2) - (Fl.height / 4)))

    wid.bind(pos=update_rect)
    wid.bind(size=update_rect)

    # draws smallest denominator lines
    with wid1.canvas:
        Color(.1, .1, .1)
        for x in range(1, denominator):
            line = Line(points=[(((width/denominator) * x) + Fl.size[0] / 5), (Fl.height * (13 / 15)),
                                (((width/denominator) * x) + Fl.size[0] / 5), (Fl.height * (5 / 18))],
                        dash_length=60, dash_offset=60, width=1, color=(.23, .6, .2))

    wid1.bind(pos=update_line)
    wid1.bind(size=update_line)

    # draws numerator box
    with wid2.canvas:
        Color(.3, .3, .6)
        rec2 = Rectangle(size=((width / denominator)*numerator, height),
                         pos=((Fl.width / 2) - (Fl.width / 3),
                              (Fl.height / 2) - (Fl.height / 4)))

    wid2.bind(pos=update_numerator)
    wid2.bind(size=update_numerator)

    # draws slider lines
    # make this a function!!

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
    width = Fl.size[0] / 5 * 2
    cwid = Widget()

    cirLabel = Label(text="each slice is 100% of the circle",
                     color=(0, 0, 0, 1),
                     font_size=62,
                     pos_hint={"x": .4, 'y': .06},
                     size_hint=(.2, .1))

    def draw():
        def update_cir(*args):
            width = Fl.size[0] / 5 * 2
            cir.pos = ((Fl.width / 2) - (Fl.width / 5),
                       (Fl.width / 2) - (Fl.width / 3))
            cir.size = (width, width)

        with cwid.canvas:
            for x in range(slider.value):
                Color(random.random(), random.random(), random.random())
                cir = Ellipse(
                    size=(width, width),
                    pos=((Fl.width / 2) - (Fl.width / 5),
                         (Fl.width / 2) - (Fl.width / 3)),
                    angle_start=(360 / slider.value) * x,
                    angle_end=((360 / slider.value) * x) +
                    (360 / slider.value),
                )
                cwid.bind(pos=update_cir)
                cwid.bind(size=update_cir)
                update_cir()

        Fl.add_widget(cwid)
        update_cir()
        return cirLabel

    def sliderValFunc(instance, val):
        sliderVal.text = "%d" % val
        Fl.remove_widget(cwid)
        cwid.canvas.clear()
        draw()
        cirLabel.text = "each slice is " + \
            str(format(100/slider.value, '.2f'))+"% of the circle"

        return sliderVal.text

    def goBack(self):
        Fl.clear_widgets()
        GameSelector(self)

    logo = Image(
        source='Images/SH_box2BSHSUName_021_horizontalstack_3_29.png',
        allow_stretch=True,
        pos_hint={'x': .01, 'y': .9},
        size_hint=(.2, .1))

    backBtnImage = Image(
        source='Images/eback-button-6-921315_2_15.png',
        pos_hint={'x': .01, 'y': .83},
        size_hint=(.04, .07),
        keep_ratio=True)

    backBtn = Button(pos_hint={"x": .01, 'y': .83},
                     size_hint=(.141, .07),
                     background_color=(1, 1, 1, .01))
    backBtn.bind(on_release=goBack)

    slider = Slider(min=1,
                    max=24,
                    step=1,
                    pos_hint={'x': .2, 'y': .15},
                    size_hint=(.6, .05))
    slider.bind(value=sliderValFunc)

    sliderVal = Label(text='1',
                      font_size=68,
                      color=(.1, .1, .1, 1),
                      pos_hint={'x': .5, 'y': .22},
                      size_hint=(.001, .001))

    draw()

    Fl.add_widget(logo)
    Fl.add_widget(backBtnImage)
    Fl.add_widget(backBtn)
    Fl.add_widget(slider)
    Fl.add_widget(sliderVal)
    Fl.add_widget(cirLabel)


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
        source='Images/SH_box2BSHSUName_021_horizontalstack_3_29.png',
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
        source='Images/eback-button-6-921315_2_15.png',
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
                # call(["python", "rip.py"])
                # os.system('python rip.py')
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
                sql = "INSERT INTO login(user,password, incorrect) VALUES('" + str(
                    userInput.text) + "',NULL, '_')"
                cursor.execute(sql)
                conn.commit()
                print("User " + str(userInput.text) + " was created!")
                global studentName
                studentName = str(userInput.text)
                GameSelector(self)
            except:
                studentName = str(userInput.text)
                studentName = str(userInput.text)
                GameSelector(self)

    logo = Image(
        source='Images/SH_box2BSHSUName_021_horizontalstack_3_29.png',
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
        source='Images/account.png',
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
