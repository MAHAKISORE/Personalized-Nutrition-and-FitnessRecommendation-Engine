from flask import Flask,request
from backend.domain.repositories.food_repository import FoodRepositoryInterface
from backend.view.config import AppConfig
from backend.domain.usecase.searchFood_usecase import SearchFoodUsecase

class FoodController:
    @staticmethod
    def create_routes(app:Flask,fpi:FoodRepositoryInterface):
        @app.route(AppConfig.search_url,methods=['GET'])
        def search():
            name = request.args.get('name')
            search_usecase = SearchFoodUsecase(upi=fpi)
            # sorted_list = FoodRepository().searchFood(name)
            sorted_list = search_usecase.searchFood(query=name)
            return sorted_list
