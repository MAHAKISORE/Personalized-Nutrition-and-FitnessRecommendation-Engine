from ..data_layer.repository.user import User
from ..data_layer.Models.user_model import UserModel


class UserAuth:
 
    def __init__(self):
        self.__data = User()

    def signIn(self,json_data):
        
        model = UserModel().fromJson(json_data=json_data)
        user = self.__data.getUser(field='email',value=model.email)
        if(user == None):
            self.__data.signIn(json_data=json_data)
            return "User successfuly created"
        else:
            return "User already exist"
        
    def login(self,json_data):
        return self.__data.login(json_data)
    
        
        
        