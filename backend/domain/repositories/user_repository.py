from abc import ABC,abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def createUser(self,json_data):
        pass

    @abstractmethod
    def getUser(self,json_data):
        pass

    @abstractmethod 
    def updateUser(self,json_data,id):
        pass

    @abstractmethod
    def updateHealthFields(self,json_data):
        pass

    @abstractmethod
    def updateFoodField(self,json_data):
        pass
   
        