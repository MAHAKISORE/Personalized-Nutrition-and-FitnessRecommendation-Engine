from .model import ModelInterface
from .user_model import UserModel

class HealthModel(UserModel,ModelInterface):
    def __init__(self,height:float=None,age:int = None,weight:float = None,bmi:float = None,allergy:int = None,diabetes:int=None,hyper_tension:int=None,gender:str = None):
        super().__init__() #initializing the parent class
        self.height:float = height
        self.weight:float = weight
        self.age:int = age
        self.bmi:float = bmi
        self.allergy:int = allergy
        self.diabetes:int = diabetes
        self.hyper_tension:int = hyper_tension
        self.gender:str = gender


    @classmethod 
    def fromJson(health, json_data):
        return health(
            height = json_data.get("height"), 
            weight = json_data.get("weight"),
            age = json_data.get("age"),
            allergy = json_data.get("allergy"),
            diabetes=  json_data.get("diabetes"),
            hyper_tension = json_data.get("hyper_tension"),
            gender = json_data.get("gender"),
            bmi = json_data.get("bmi")
        )
