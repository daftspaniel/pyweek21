import sqlite3
import os.path


class AftermathWorld(object):
    def __init__(self, filename):
        self.Filename = filename
        self.isNewWorld = not os.path.isfile(amw.Filename)

    def create(self):
        conn = sqlite3.connect(amw.Filename)
        self.createTables(conn)
        self.createAmy(conn)
        conn.close()

    def createAmy(self, conn):
        conn.execute()

    def createTables(self, conn):
        conn.execute('''CREATE TABLE WORLD
                       (ID INT PRIMARY KEY     NOT NULL,
                        DAY              INT     NOT NULL,
                        HOUR             INT     NOT NULL
                       );''')
        conn.execute('''CREATE TABLE CHARACTER
                       (ID INT PRIMARY KEY     NOT NULL,
                        NAME           TEXT    NOT NULL,
                        X              INT     NOT NULL,
                        Y              INT     NOT NULL,
                        SPIRIT            INT     NOT NULL
                       );''')


if __name__ == "__main__":
    amw = AftermathWorld('world.db')

    if amw.isNewWorld:
        amw.create()
    else:
        print("Found Existing World")
