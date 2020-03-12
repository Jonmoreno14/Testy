from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
import sqlite3

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

            self.data = [{'text': str(row[0]), 'color': (0, 0, 0, 1)}
                         for row in records]
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
