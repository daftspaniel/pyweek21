import sqlite3
import os.path


class AftermathWorld(object):
    def __init__(self, filename):
        self.Filename = filename
        self.isNewWorld = not os.path.isfile(self.Filename)

    def create(self):
        self.connect()
        self.createTables()
        self.createCharacters()
        self.display()
        self.conn.close()

    def connect(self):
        self.conn = sqlite3.connect(self.Filename)

    def createCharacters(self):
        self.conn.execute("""
                      INSERT INTO CHARACTER (ID,NAME,X,Y,SPIRIT)
                      VALUES (1, 'Amy', 10, 10, 99)
                    """)
        self.conn.execute("""
                      INSERT INTO CHARACTER (ID,NAME,X,Y,SPIRIT)
                      VALUES (2, 'Bill', 6, 8, 70)
                    """)
        self.conn.execute("""
                      INSERT INTO CHARACTER (ID,NAME,X,Y,SPIRIT)
                      VALUES (3, 'Cam', 7, 8, 70)
                    """)
        self.conn.commit()

    def createTables(self):
        self.conn.execute('''CREATE TABLE WORLD
                       (ID               INT PRIMARY KEY     NOT NULL,
                        DAY              INT     NOT NULL,
                        HOUR             INT     NOT NULL
                       );''')
        self.conn.execute('''CREATE TABLE CHARACTER
                       (ID             INT PRIMARY KEY     NOT NULL,
                        NAME           TEXT    NOT NULL,
                        X              INT     NOT NULL,
                        Y              INT     NOT NULL,
                        SPIRIT         INT     NOT NULL
                       );''')

    def display(self):
        self.connect()

        cursor = self.conn.execute("SELECT * FROM CHARACTER")
        for row in cursor:
            print(row)
        self.conn.close()

    def get_characters(self):
        self.connect()
        rs = []
        cursor = self.conn.execute("SELECT * FROM CHARACTER")
        for row in cursor:
            rs.append(row)
        self.conn.close()
        return rs

    def save(self, game):
        self.connect()
        for character in game["characters"]:
            self.conn.execute("UPDATE CHARACTER SET X="
                              + str(character[1]) +
                              ", Y=" + str(character[2]) +
                              " where ID=" + str(character[0]))
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":

    amw = AftermathWorld('world.db')

    if amw.isNewWorld:
        amw.create()
    else:
        print("Found Existing World")
