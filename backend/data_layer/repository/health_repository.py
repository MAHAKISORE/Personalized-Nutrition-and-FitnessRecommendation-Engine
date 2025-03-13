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

        try:
            health_data:HealthModel = HealthModel.fromJson(json_data=json_data)
            health_data.bmi =self.bmi(height=health_data.height,weight=health_data.weight)
            self._cursor.execute("UPDATE Users SET gender=?,height=?,weight=?,age=?,bmi=?,allergy=?,diabetes=?,hyper_tension=? WHERE id=?",(health_data.gender,health_data.height,health_data.weight,health_data.age,health_data.bmi,health_data.allergy,health_data.diabetes,health_data.hyper_tension,json_data["id"]))
            self._conn.commit()
        except Exception as e:
                print(e)
        finally:
             self._conn.close()
             
        


