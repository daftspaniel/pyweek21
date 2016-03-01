import sqlite3
import os.path


class AftermathWorld(object):
    def __init__(self, filename):
        self.Filename = filename
        self.isNewWorld = not os.path.isfile(self.Filename)

    def create(self):
        self.conn = sqlite3.connect(self.Filename)
        self.createTables()
        self.createCharacters()
        self.display()
        self.conn.close()

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
        self.conn = sqlite3.connect(self.Filename)

        cursor = self.conn.execute("SELECT * FROM CHARACTER")
        for row in cursor:
           print(row)
        self.conn.close()
    def get_characters(self):
        self.conn = sqlite3.connect(self.Filename)
        rs = []
        cursor = self.conn.execute("SELECT * FROM CHARACTER")
        for row in cursor:
           rs.append(row)
        self.conn.close()
        return rs

    def save(self):
        self.conn = sqlite3.connect(self.Filename)
        self.conn.execute("UPDATE CHARACTER SET X=5, Y=5 where ID=1")
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":

    amw = AftermathWorld('world.db')

    if amw.isNewWorld:
        amw.create()
    else:
        print("Found Existing World")

