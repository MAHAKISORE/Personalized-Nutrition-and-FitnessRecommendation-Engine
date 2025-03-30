from...view.config import AppConfig
from abc import ABC,abstractmethod
from ...data.repositories.food_repository import FoodRepository



class SearchFoodUsecase():
    def __init__(self):
        self.user_repo = FoodRepository()

    def searchFood(self,query):
        if(query == None or query == ""):
            return {"data":""},AppConfig.ok_code
        filtered_data = self.user_repo.searchFood(query=query)
        return filtered_data

