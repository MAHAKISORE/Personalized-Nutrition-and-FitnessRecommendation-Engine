from database.user import User
from Models.user_model import UserModel


class UserAuth:
 
    def __init__(self):
        pass

    def signIn(self,json_data):
        data = User()
        model = UserModel().fromJson(json_data=json_data)
        user = data.getUser("phone",model.phone)
        if(len(user) == 0):
            data.signIn(json_data=json_data)
            return "User successfuly created"
        else:
            return "User already exist"
        
        
        