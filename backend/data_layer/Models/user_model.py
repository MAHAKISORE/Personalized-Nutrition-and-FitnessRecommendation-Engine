import random
from .model import ModelInterface

class UserModel(ModelInterface):
    def __init__(self,id:str = None,name:str = None,age:int = None,height:float=None,weight:float=None,email:str = None,gender:str = None):
        self.id = id
        self.name:str = name
        self.age:int = age
        self.height:float = height
        self.weight:float = weight
        self.email:int = email
        self.gender:str = gender

    def toDatabase(self,json_data):
        id = random.randint(1000,99999)
        user = self.fromJson(json_data)
       
        return(id,user.name,user.email)

    # @classmethod
    # def fromDatabase(user,data):
       
    #     return user(
    #         id = data.get('id'),
    #         name = data.get('name'),
    #         age = data.get('age'),
    #         height = data.get('height'),
    #         weight=data.get('weight'),
    #         email = data.get('email'),
    #         gender = data.get('gender')
    #     )
    

    
    @classmethod
    def fromJson(user,json_data):
        print(json_data.get("name"))
        return user(
            name=json_data.get("name"),
            age=json_data.get("age"),
            height = json_data.get("height"),
            weight = json_data.get("weight"),
            email = json_data.get("email"),
            gender = json_data.get("gender")
            ) 
    

    

