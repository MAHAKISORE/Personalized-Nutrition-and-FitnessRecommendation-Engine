from ..data_sources.user_datasource import UserDatasource
from ..data_sources.health_datasource import HealthDatasource
from ..data_sources.food_datasource import FoodDatasource
from ...domain.repositories.user_repository import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self):
        self.user_datasource = UserDatasource()
        self.health_datasource = HealthDatasource()
        self.food_datasource = FoodDatasource()

    def createUser(self,json_data):
        return self.user_datasource.createUser(json_data=json_data)
    
    def getUser(self,field,value):
        return self.user_datasource.getUser(field=field,value=value)
    
    def updateUser(self,json_data,id):
        self.user_datasource.updateUser(json_data=json_data,id=id)

    def updateHealthFields(self,json_data):
        self.health_datasource.updateHealthFields(json_data=json_data)

    def updateFoodField(self,json_data):
        self.food_datasource.updateFoodField(json_data=json_data)
    
