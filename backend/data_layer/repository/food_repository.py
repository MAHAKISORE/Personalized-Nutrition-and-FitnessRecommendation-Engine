from .db import DataBase
from .jaro import JaroWrinklerSearching

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
        jaro_search = JaroWrinklerSearching(data)
        sorted_list = jaro_search.hybrid_search(query=query)
        return sorted_list
    

