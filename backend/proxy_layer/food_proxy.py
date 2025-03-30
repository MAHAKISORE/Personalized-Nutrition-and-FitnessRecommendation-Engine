from ..data_layer.repository.caching_repository import CachingRepository
from ..data_layer.repository.food_repository import FoodRepository
from ..data_layer.Models.food_model import FoodModel

class FoodProxy:
    def __init__(self):
        self.cache_repository = CachingRepository()
        self.food_repository = FoodRepository()
    
    def searchFood(self,query):
        cached_data = self.cache_repository.getJsonCacheData("food")
        if(cached_data != None):
            print("Used cached data")
        if(cached_data == None):
            db_data = self.food_repository.getData()
            datas = []
            for i in db_data:
                datas.append(FoodModel.toJson(i))
            cached_data = self.cache_repository.setJsonData("food",datas)
        searched_data = self.food_repository.searchFood(db_data=cached_data,query=query)
        return searched_data