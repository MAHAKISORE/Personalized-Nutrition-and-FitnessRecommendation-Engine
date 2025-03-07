from abc import ABC,abstractmethod



class ModelInterface(ABC):

    @classmethod
    @abstractmethod
    def fromJson(self,data):
        pass

    # @classmethod
    # @abstractmethod
    # def fromDatabase(self,data):
    #     pass
    

    @abstractmethod
    def toDatabase(self,json_data):
        pass



















































































    