import sqlite3


def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('UserInfo.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from Login"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            print("User: ", row[0])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)


readSqliteTable()
