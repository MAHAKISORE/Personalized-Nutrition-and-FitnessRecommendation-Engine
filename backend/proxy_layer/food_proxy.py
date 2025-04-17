from ..data_layer.repository.caching_repository import CachingRepository
from ..data_layer.repository.food_repository import FoodRepository
from ..data_layer.Models.food_model import FoodModel
from ..data_layer.repository.irepositories.ifood_repository import FoodRepositoryInterface


class FoodProxy(FoodRepositoryInterface):
    def __init__(self):
        self.cache_repository = CachingRepository()
        self.food_repository = FoodRepository()
    
    def searchFood(self,query):
        cached_data = self.cache_repository.getJsonCacheData("food")

        if(cached_data == None):
            db_data = self.food_repository.getData()
            datas = []
            for i in db_data:
                datas.append(FoodModel.toJson(i))
            self.cache_repository.setJsonData("food",datas)
            print(datas)
            print("User cached")
            return datas
        
        searched_data = self.food_repository.searchFood(db_data=cached_data,query=query)
        print(searched_data)
        return searched_data
    
    