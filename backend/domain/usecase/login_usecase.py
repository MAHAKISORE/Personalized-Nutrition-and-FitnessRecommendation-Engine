from ...data.repositories.user_repository import UserRepository
from ...data.Models.user_model import UserModel
from ...view.config import AppConfig
from backend.domain.repositories.user_repository import UserRepositoryInterface



class LoginUsecase():
    
    def __init__(self,upi:UserRepositoryInterface):
        self.__data =upi
       
        
    def login(self,json_data):
        email = json_data["email"]
        pwd = json_data["pwd"]

        user = self.__data.getUser("email",email)
        if(user == None):
            return {"ms":"Email has not been registered yet"},AppConfig.bad_request_code
        
        if(user[6] == pwd):
            return {"id":user[0]},AppConfig.ok_code
        else:
            return {"msg":"Wrong pwd"},AppConfig.unauthorized_code
    
        
        
        