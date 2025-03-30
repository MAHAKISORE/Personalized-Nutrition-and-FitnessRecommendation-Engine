from ..data_sources.redis_datasource import RedisDatasource
from ..data_sources.food_datasource import FoodDatasource
from ..Models.food_model import FoodModel
from ...domain.repositories.food_repository import FoodRepositoryInterface

class FoodRepository(FoodRepositoryInterface):
    def __init__(self):
        self.cache_repository = RedisDatasource()
        self.food_repository = FoodDatasource()
    
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
    