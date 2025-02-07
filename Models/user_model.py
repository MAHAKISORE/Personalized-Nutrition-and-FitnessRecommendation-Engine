import random


class UserModel:
    def __init__(self,name:str = None,age:int = None,height:float=None,weight:float=None,email:int = None,gender:str = None):
        self.id = None
        self.name:str = name
        self.age:int = age
        self.height:float = height
        self.weight:float = weight
        self.email:int = email
        self.gender:str = gender

    def toDataBase(self,json_data):
        id = random.randint(1000,99999)
        user = self.fromJson(json_data)
        return(id,user.name,user.email,user.age,user.weight,user.gender)
    
    @classmethod
    def fromJson(user,json_data):
        return user(
            name=json_data["name"],
            age=json_data["age"],
            height = json_data["height"],
            weight = json_data["weight"],
            email = json_data["email"],
            gender = json_data["gender"]
            
            )
    

    

