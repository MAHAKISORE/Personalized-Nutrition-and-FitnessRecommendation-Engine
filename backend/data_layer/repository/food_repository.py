from .db import DataBase
from .jaro import JaroWrinklerSearching
from ..Models.food_model import FoodModel
from abc import ABC,abstractmethod


class FoodRepositoryInterface(ABC):
    @abstractmethod
    def getData(self):
        pass
    @abstractmethod
    def search_data(self,query):
        pass

    @abstractmethod
    def updateFoodField(self,json_data):
        pass

class FoodRepository(FoodRepositoryInterface,DataBase):

    def __new__(cls):
        if not hasattr(cls,"food_instance"):
            cls.food_instance = super(FoodRepository,cls).__new__(cls)
        return cls.food_instance

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


    def updateFoodField(self,json_data):
        model = FoodModel.jsonToUpdate(json_data = json_data,query_value=json_data.get("id"))
        task = f"UPDATE Users SET {model.columns} WHERE id=?"
        self._cursor.execute(task,model.values)
        self._conn.commit()
        