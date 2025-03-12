from .model import ModelInterface

class FoodModel(ModelInterface):
    def __init__(self,id:str = None,name:str = None,energy:float= None,calorie:float=None,protien:float = None):
        #instance variables
        self.id:int = id
        self.name:str = name,
        self.energy:float = energy
        self.calorie:float = calorie,
        self.protien:float = protien
    
    def toDatabase(self, json_data):
        data = self.fromJson(json_data)
        return (data.id,data.name,data.calorie,)
    
    @classmethod
    def fromDatabase(user,data):
        return user(data[0],data[1],data[2],data[3],data[4]) 
    
    @classmethod
    def fromJson(food,json_data):
        return food(
            id=json_data.get("id"),
            name=json_data.get("name"),
            energy = json_data.get("energy"),
            calorie = json_data.get("calorie"),
            protien = json_data.get("protien"),)
    
            