from ..data_layer.repository.food_repository import FoodRepository
from..view.config import AppConfig
from abc import ABC,abstractmethod


class FoodControllerInterface(ABC):
    @abstractmethod
    def updateFood(self,json_data):
        pass


class FoodController(FoodControllerInterface):
    def __init__(self):
        self.food_repo = FoodRepository()

    def updateFood(self,json_data):
        if(json_data.get("id") == None):
            return {"msg":"Id is required to update"},AppConfig.bad_request_code
        self.food_repo.updateFoodField(json_data=json_data)
        return {"msg":"Ok"},AppConfig.ok_code
    
