from ...data.repositories.user_repository import UserRepository
from abc import ABC,abstractmethod
from ...view.config import AppConfig
from backend.domain.repositories.user_repository import UserRepositoryInterface


# class HealthControllerInterface(ABC):
#      @abstractmethod
#      def updateHealthModel(self,json_data):
#           pass
     

class UpdateHealthUsecase():
    def __init__(self,upi:UserRepositoryInterface):
        self.heath_repository = upi

    def updateHealthModel(self,json_data):
            if(self.heath_repository.getUser("id",json_data["id"])): 
                self.heath_repository.updateHealthFields(json_data=json_data)
                return {"msg":"Updated"},AppConfig.ok_code
            else:
                 return {"msg":"Invalid id"},AppConfig.unauthorized_code