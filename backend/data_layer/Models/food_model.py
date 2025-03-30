from .model import ModelInterface

class FoodModel(ModelInterface):
    def __init__(self,id:str = None,name:str = None,energy:float= None,calorie:float=None,protien:float = None):
        #instance variables
        self.id:int = id
        self.name:str = name,
        self.energy:float = energy
        self.calorie:float = calorie,
        self.protien:float = protien,
        self.similarity:int = None

    # def __str__(self):
    #       return f"id:{self.id},name:{self.name}"
 

    @classmethod
    def fromJson(food,json_data):
        return food(
            id=json_data["food_code"],
            name=json_data["food_name"],
            energy = json_data["energy_kj"],
            calorie = json_data["energy_kcal"],
            protien = json_data["protein_g"])
    
    def toDatabase(self, json_data):
            pass
    
    
    def toJson(self):
          return {
                "food_code":self.id,
                "food_name":self.name,
                "energy_kj":self.energy,
                "energy_kcal":self.calorie,
                "protein_g":self.protien
          }

    @classmethod
    def stringToList(food,text:str):
            converted_data = [[int(y) for y in x.split(",")] for x in text.split(";")]
            return converted_data
    
    # def toDatabase(self, json_data):
    #     data = self.fromJson(json_data)
    #     return (data.id,data.name,data.calorie,)
    
    # @classmethod
    # def fromDatabase(user,data):
    #     return user(data[0],data[1],data[2],data[3],data[4]) 
    
    # @classmethod
    # def fromJson(food,json_data):
    #     return food(
    #         id=json_data.get("id"),
    #         name=json_data.get("name"),
    #         energy = json_data.get("energy"),
    #         calorie = json_data.get("calorie"),
    #         protien = json_data.get("protien"),)