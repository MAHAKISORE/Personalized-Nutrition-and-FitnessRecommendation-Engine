from ...data.repositories.user_repository import UserRepository
from ...data.Models.user_model import UserModel
from ...view.config import AppConfig


class SignInUsecase():
    
    def __init__(self):
        self.__data = UserRepository()

    def signIn(self,json_data):
            model = UserModel().fromJson(json_data=json_data)
            if(not model.emailValid):
                 return {"msg":"Invalid email address"},AppConfig.bad_request_code
            user = self.__data.getUser(field='email',value=model.email)
            if(user == None):
                user = self.__data.signIn(json_data=json_data)
                print(user)
                return {"id":user},201
            else:
                return {"msg":"User already exist"},AppConfig.conflict_code
       
   