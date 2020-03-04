#!/usr/local/bin/python3
#import numpy as np
#import sys as plt
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
#sys.path.append('/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/matplotlib')
#import matplotlib.pyplot as plt
#from matplotlib.widgets import TextBox
import imp
util = imp.load_source('util', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/matplotlib')
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        box = BoxLayout()
        l = Label(text='g')
        box.add_widget(l)
        box.add_widget(FigureCanvasKivyAgg(util.gcf()))
        return box

MyApp().run()