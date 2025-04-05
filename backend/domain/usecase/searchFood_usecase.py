from...view.config import AppConfig
from backend.domain.repositories.food_repository import FoodRepositoryInterface


class SearchFoodUsecase():
    def __init__(self,upi:FoodRepositoryInterface):
        self.user_repo = upi

    def searchFood(self,query):
        if(query == None or query == ""):
            return {"data":""},AppConfig.ok_code
        filtered_data = self.user_repo.searchFood(query=query)
        return filtered_data

