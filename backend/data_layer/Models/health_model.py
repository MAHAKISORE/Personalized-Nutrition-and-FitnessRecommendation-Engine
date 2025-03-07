from .model import ModelInterface
from .user_model import UserModel

class HealthModel(UserModel):
    def __init__(self,height:float=None,age:int = None,weight:float = None,bmi:float = None,allergy:int = None,diabetes:int=None,hyper_tension:int=None,gender:str = None):
        super().__init__()
        self.height = height
        self.weight = weight
        self.age = age
        self.bmi = bmi
        self.allergy = allergy
        self.diabetes = diabetes
        self.hyper_tension = hyper_tension
        self.gender = gender
    
    def __str__(self):
        return str(self.age)
    

    @classmethod
    def fromJson(health, json_data):
        return health(
            height = json_data.get("height"),
            weight = json_data.get("weight"),
            age = json_data.get("age"),
            allergy = json_data.get("allergy"),
            diabetes=  json_data.get("diabetes"),
            hyper_tension = json_data.get("hyper_tension"),
            gender = json_data.get("gender")
        )

    def toDatabase(self, json_data,id):
        data = self.fromJson(json_data)
        return (data.height,data.weight,data.age,data.bmi,data.allergy,data.diabetes,data.hyper_tension,id)
    
    # @classmethod
    # def fromDatabase(user,data):
    #     return user(data[0],data[1],data[2],data[3],data[4],data[5],data[6]) 