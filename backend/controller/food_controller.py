from ..data_layer.repository.food_repository import FoodRepository
from..view.config import AppConfig
from abc import ABC,abstractmethod
# from ..proxy_layer.food_proxy import FoodProxy


class FoodControllerInterface(ABC):
    @abstractmethod
    def updateFood(self,json_data):
        pass


class FoodController(FoodControllerInterface):
    def __init__(self):
        self.food_repo = FoodRepository()
        # self.food_proxy = FoodProxy()

    def updateFood(self,json_data):
        if(json_data.get("id") == None):
            return {"msg":"Id is required to update"},AppConfig.bad_request_code
        self.food_repo.updateFoodField(json_data=json_data)
        return {"msg":"Ok"},AppConfig.ok_code
    
    def searchFood(self,query):
        if(query == None or query == ""):
            return {"data":""},AppConfig.ok_code
        data = self.food_repo.getData()
        filtered_data = self.food_repo.searchFood(query=query,db_data=data)
        return filtered_data


    def high_protein_diet(self,json_data,calorie):
        if(calorie == 0 or calorie == None):
            return {"msg":"Invalid calorie"},AppConfig.bad_request_code
        high_protein_foods = self.food_repo.knapsack_food(json_data,calorie=calorie)
        return {"msg":high_protein_foods},AppConfig.ok_code
    
    def get_diet(self,id):
        return self.food_repo.set_diet(id=id)
