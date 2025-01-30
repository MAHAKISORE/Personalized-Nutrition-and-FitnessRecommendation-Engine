from .db import DataBase

class User(DataBase):
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()

    def signIn(self):
        self._cursor.execute("INSERT INTO Users VALUES(5457654,'Kishore',8248001758,78,90,'M')")
        self._conn.commit()

        

