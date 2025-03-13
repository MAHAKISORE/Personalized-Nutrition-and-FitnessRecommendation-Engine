from ..data_layer.repository.health_repository import HealthRepository
from ..data_layer.repository.user_repository import UserRepository
from abc import ABC,abstractmethod


class HealthControllerInterface(ABC):
     @abstractmethod
     def updateHealthModel(self,json_data):
          pass
     

class HealthController(HealthControllerInterface):
    def __init__(self):
        self.heath_repository = HealthRepository()

    def updateHealthModel(self,json_data):
            # print(json_data["id"])
            if(self.heath_repository.getUser("id",json_data["id"])): 
                health = self.heath_repository.updateHealthFields(json_data=json_data)
                return "Updated"
            else:
                 return "Invalid id"