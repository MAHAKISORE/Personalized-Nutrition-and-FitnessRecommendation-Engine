from db import DataBase


class Foods(DataBase):
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()
        self.data = []

    def getData(self):
        task = "SELECT food_name FROM Foods"
        self._cursor.execute(task)
        data:list = self._cursor.fetchall()
        for i in data:
            for k in i:
                self.data.append(k)



