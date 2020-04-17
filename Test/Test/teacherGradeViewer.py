from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
import sqlite3
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget


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


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        try:
            conn = sqlite3.connect('UserInfo.db')
            cursor = conn.cursor()
            sqlite_select_query = """SELECT * from Login"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()

            for row in records:
                print(row[0])
                print(row[1])
                print(row[2])

                '''
                if str(row[2]) == "None":
                    pass
                else:
                    self.data = [
                        {'text': str(row[0]) + " Incorrect: " + str(row[2]), 'color': (0, 0, 0, 1)}]
            '''
            '''
            self.data = [{'text': str(row[0]) + " Incorrect: " + str(row[2]), 'color': (0, 0, 0, 1)}
                         for row in records]
            '''
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table")


class TestApp(App):
    def build(self):
        return RV()


def runApp():
    TestApp().run()
# if __name__ == '__main__':
#   TestApp().run()
