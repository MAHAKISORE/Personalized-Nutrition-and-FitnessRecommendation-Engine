from ..Models.health_model import HealthModel
from abc import ABC,abstractmethod
from .user_repository import UserRepository

class HeatlthRepositoryInterface(ABC):
     @abstractmethod
     def bmi(self):
          pass
     @abstractmethod
     def updateHealthFields(self):
          pass
     

class HealthRepository(UserRepository,HeatlthRepositoryInterface):
    def __init__(self):
        super().__init__()
    
    def bmi(self,height,weight):
        return weight/(height*height)
    
    def updateHealthFields(self,json_data):

        
            updates = HealthModel.jsonToUpdate(json_data=json_data,query_value=json_data["id"])
            print(f"UPDATE Users SET {updates.columns} WHERE id=?",updates.values)
            # health_data:HealthModel = HealthModel.fromJson(json_data=json_data)
            # health_data.bmi =self.bmi(height=health_data.height,weight=health_data.weight)
            self._cursor.execute(f"UPDATE Users SET {updates.columns} WHERE id=?",updates.values)
            self._conn.commit()
       
        #      self._conn.close()
             
        


