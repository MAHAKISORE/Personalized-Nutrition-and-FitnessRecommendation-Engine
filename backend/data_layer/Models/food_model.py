from .model import Models

class FoodModel(Models):
    def __init__(self,id:str = None,name:str = None,energy:float= None,calorie:float=None,protien:float = None):
        self.id = id
        self.name = name,
        self.energy = energy
        self.calorie = calorie,
        self.protien = protien
    
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
    
            