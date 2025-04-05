from...view.config import AppConfig
from backend.domain.repositories.user_repository import UserRepositoryInterface



class UpdateFoodUsecase():
    def __init__(self,user_repo:UserRepositoryInterface):
        self.user_repo = user_repo

    def updateFood(self,json_data):
        if(json_data.get("id") == None):
            return {"msg":"Id is required to update"},AppConfig.bad_request_code
        self.user_repo.updateFoodField(json_data=json_data)
        return {"msg":"Ok"},AppConfig.ok_code
    
 
