from ..data_layer.repository.health_repository import HealthRepository
from ..data_layer.repository.user_repository import UserRepository
from abc import ABC,abstractmethod


class HealthControllerInterface(ABC):
     @abstractmethod
     def updateHealthModel(self,json_data):
          pass
     

class HealthController(HealthRepository,HealthControllerInterface):
    def __init__(self):
        self.heath_repository = HealthRepository()

    def updateHealthModel(self,json_data):
            # print(json_data["id"])
            self.heath_repository.updateHeathFields(json_data=json_data)
            return "Updated!"