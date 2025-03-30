from ...data.repositories.user_repository import UserRepository
from abc import ABC,abstractmethod
from ...view.config import AppConfig


# class HealthControllerInterface(ABC):
#      @abstractmethod
#      def updateHealthModel(self,json_data):
#           pass
     

class UpdateHealthUsecase():
    def __init__(self):
        self.heath_repository = UserRepository()

    def updateHealthModel(self,json_data):
            if(self.heath_repository.getUser("id",json_data["id"])): 
                self.heath_repository.updateHealthFields(json_data=json_data)
                return {"msg":"Updated"},AppConfig.ok_code
            else:
                 return {"msg":"Invalid id"},AppConfig.unauthorized_code