from ..data_layer.repository.user_repository import UserRepository
from ..data_layer.Models.user_model import UserModel
from abc import ABC, abstractmethod


class UserAuthInterface(ABC):
    @abstractmethod
    def signIn(self,json_data):
        pass
    @abstractmethod
    def login(self,json_data):
        pass


class UserAuth(UserAuthInterface):
    
    def __init__(self):
        self.__data = UserRepository()

    def signIn(self,json_data):
            model = UserModel().fromJson(json_data=json_data)
            
            user = self.__data.getUser(field='email',value=model.email)
            if(user == None):
                user = self.__data.signIn(json_data=json_data)
                print(user)
                return user
            else:
                return "User already exist"
       
        
    def login(self,json_data):
        email = json_data["email"]
        pwd = json_data["pwd"]

        user = self.__data.getUser("email",email)
        if(user == None):
            return "Email has not been registered yet"
        
        if(user[6] == pwd):
            return "User verified"
        else:
            return "Wrong pwd"
    
        
        
        