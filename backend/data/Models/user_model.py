import random
from .model import ModelInterface
from ...domain.entities.user_entitie import UserEntitie

class UserModel(ModelInterface,UserEntitie):
    def __init__(self,id:int = None,name:str = None,email:str = None):
        super().__init__(
            id=id,
            name=name,
            email=email
        )
      

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
            id = json_data.get("id"),
            name=json_data.get("name"),
            email = json_data.get("email"),
            ) 
    

    

