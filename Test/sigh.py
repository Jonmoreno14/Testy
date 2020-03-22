from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
import sqlite3
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window

Fl = FloatLayout()
Window.clearcolor = (1, 1, 1, 1)
Window.size = (1200, 800)


def MainWindow(self):
    Builder.load_string('''
<RV>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(36)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')
    self.data = [{'text': "str(row[0])", 'color': (0, 0, 0, 1)}]
    Fl.add_widget(Button(text="text"))


class MyMainApp(App):
    def build(self):

        return Fl


if __name__ == "__main__":
    MyMainApp().run()
