from ..data_layer.repository.health_repository import HealthRepository
from ..data_layer.repository.user_repository import UserRepository
from abc import ABC,abstractmethod
from ..view.config import AppConfig


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
                self.heath_repository.updateHealthFields(json_data=json_data)
                return {"msg":"Updated"},AppConfig.ok_code
            else:
                 return {"msg":"Invalid id"},AppConfig.unauthorized_code