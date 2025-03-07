from .db import DataBase
from .jaro import hybrid_search

class Foods(DataBase):
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()
      

    def getData(self):
        datas = []
        task = "SELECT food_name FROM Foods"
        self._cursor.execute(task)
        data:list = self._cursor.fetchall()
        for i in data:
            for k in i:
                datas.append(k)
        return datas
    def search_data(self,query):
        data = self.getData()
        sorted_list = hybrid_search(query=query,name_list=data,top_n=20)
        return sorted_list