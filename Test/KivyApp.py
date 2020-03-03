from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
import sqlite3
import hashlib
Window.clearcolor = (1, 1, 1, 1)
Window.size = (1200, 800)

conn = sqlite3.connect("UserInfo.db")
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS login(user TEXT NOT NULL UNIQUE, password TEXT);"
)

Fl = FloatLayout()

class GameSelector():
    def miniMenu():
        Fl.clear_widgets()

        logo =  Image(source = '/Users/jonathonmoreno/Desktop/SE/Test/Images/SH_box2BSHSUName_021_horizontalstack_3_29.png', 
                    allow_stretch= True, pos_hint= {"x": .01, 'y':.9}, size_hint=(.2, .1))
        fractionEq = Button(text='Fraction Equivilence',pos_hint = {"x": .3, 'y':.6}, font_size=46 ,size_hint =  (.4, .25), color = (0, 0, 0, 1),
                    background_color = (1, 1, 1, .6))

        pieFraction = Button(text='Pie Fractions',pos_hint = {"x": .3, 'y':.2}, font_size=46 ,size_hint =  (.4, .25), color = (0, 0, 0, 1),
                    background_color = (1, 1, 1, .6))

        backBtnImage = Image(source = '/Users/jonathonmoreno/Desktop/SE/Test/Images/eback-button-6-921315_2_15.png',pos_hint = {"x": .01, 'y':.83}, size_hint =  (.04, .07),
                  keep_ratio = True)

        backBtn = Button(pos_hint = {"x": .01, 'y':.83}, size_hint =  (.141, .07),
                        background_color = (1, 1, 1, .01))
        backBtn.bind(on_release=MainWindow)
        
        Fl.add_widget(logo)
        Fl.add_widget(fractionEq)
        Fl.add_widget(pieFraction)
        Fl.add_widget(backBtnImage)
        Fl.add_widget(backBtn)

        

class FractionEq():
    pass

class PieFraction():
    pass

class MainWindow():
    
    def teacherFunc(self): 

        def submitFunc2(self):
            encrypted = hashlib.md5(str(passInput.text).encode("utf-8")).hexdigest()
            sql = "SELECT * FROM login WHERE user = '"+str(MainWindow.userInput.text)+"' AND password = '"+encrypted+"'"
            cursor.execute(sql)
            conn.commit()
            if cursor.fetchone() is not None:
                print("Welcome")
            else:
                wrong = Label(text='Incorrect password!', color= (1, 0, 0, 1),
                    pos_hint= {"x": .4, 'y':.25}, font_size=36 , size_hint= (.2, .1))
                Fl.add_widget(wrong)
            GameSelector()
        
            
        Fl.remove_widget(MainWindow.submitBtn)
        passLabel = Label(text='Enter your password:', color= (0, 0, 0, 1),
                    pos_hint= {"x": .01, 'y':.35}, font_size=46 , size_hint= (.2, .1))

        passInput = TextInput(multiline = False, pos_hint = {"x": .3, 'y':.36}, 
                    font_size = 46, size_hint = (.4, .07), password = True, cursor_blink = True, padding_x=50, padding_y=30, write_tab = False)

        submitBtn = Button(text = "Submit",pos_hint = {"x": .38, 'y':.03}, size_hint =  (.25, .15), color = (0, 0, 0, 1),
                    background_color = (1, 1, 1, .6))
        submitBtn.bind(on_release=submitFunc2)

        Fl.add_widget(passLabel)
        Fl.add_widget(passInput)
        Fl.add_widget(submitBtn)

    def submitFunc(self):
        try:
            sql = "INSERT INTO login(user,password) VALUES('"+str(MainWindow.userInput.text)+"',NULL)"
            cursor.execute(sql)
            conn.commit()
            print("User "+str(MainWindow.userInput.text) + " was created!")
            GameSelector.miniMenu()
        except:
            wrong = Label(text='Enter your name!', color= (1, 0, 0, 1),
                    pos_hint= {"x": .4, 'y':.25}, font_size=36 , size_hint= (.2, .1))
            Fl.add_widget(wrong)

    logo =      Image(source = '/Users/jonathonmoreno/Desktop/SE/Test/Images/SH_box2BSHSUName_021_horizontalstack_3_29.png', 
                allow_stretch= True, pos_hint= {"x": .01, 'y':.9}, size_hint=(.2, .1))

    userLabel = Label(text='Enter your name:', color= (0, 0, 0, 1),
                pos_hint= {"x": .026, 'y':.59}, font_size=46 , size_hint= (.2, .1))

    userInput = TextInput(multiline = False, pos_hint = {"x": .30, 'y':.6}, 
                font_size = 46, size_hint = (.4, .07), cursor_blink = True, padding_x=50, padding_y=30, write_tab = False)

    submitBtn = Button(text = "Submit",pos_hint = {"x": .38, 'y':.03}, size_hint =  (.25, .15), color = (0, 0, 0, 1),
                background_color = (1, 1, 1, .6))
    submitBtn.bind(on_release=submitFunc)

    teacherHead = Image(source = '/Users/jonathonmoreno/Desktop/SE/Test/Images/account.png',pos_hint = {"x": .9, 'y':.03}, size_hint =  (.04, .07),
                keep_ratio = True)

    teacherHeadBtn = Button(pos_hint = {"x": .80, 'y':.03}, size_hint =  (.141, .07),
                background_color = (1, 1, 1, .01))
    teacherHeadBtn.bind(on_release=teacherFunc)

    teacherLabel = Label(text="Teacher Login", color= (0, 0, 0, 1),pos_hint = {"x": .75, 'y':.018}, font_size=30 , size_hint= (.2, .1))

    Fl.add_widget(userLabel)
    Fl.add_widget(logo)
    Fl.add_widget(userInput)
    Fl.add_widget(submitBtn)
    Fl.add_widget(teacherHeadBtn)
    Fl.add_widget(teacherHead)
    Fl.add_widget(teacherLabel)
    

class MyMainApp(App):
    def build(self):
        self.title = 'Fractions'
        return Fl

if __name__ == "__main__":
    MyMainApp().run()
