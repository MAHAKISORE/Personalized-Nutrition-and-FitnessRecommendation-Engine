from .model import ModelInterface

class FoodModel(ModelInterface):
    def __init__(self,food_code:str=None,id:str = None,name:str = None,energy:float= None,calorie:float=None,protien:float = None):
        #instance variables
        self.id = id
        self.food_code:str = food_code
        self.name:str = name
        self.energy:float = energy
        self.calorie:float = calorie
        self.protien:float = protien
        self.similarity:int = None

    def __str__(self):
          return f"id:{self.id},name:{self.calorie}"
 

    @classmethod
    def fromJson(food,json_data):
        return food(
            id = json_data["id"],
            food_code=json_data["food_code"],
            name=json_data["food_name"],
            energy = json_data["energy_kj"],
            calorie = json_data["energy_kcal"],
            protien = json_data["protein_g"])
    
    def toDatabase(self, json_data):
            pass
    
    
    def toJson(self):
          return {
                "id":self.id,
                "food_code":self.food_code,
                "food_name":self.name,
                "energy_kj":self.energy,
                "energy_kcal":self.calorie,
                "protein_g":self.protien
          }

    @classmethod
    def stringToList(food,text:str):
            converted_data = [[[int(y) for y in x.split(",")] for x in k.split(";")] for k in text.split("/")]
            return converted_data
    
    @classmethod
    def listMaptoFood(cls,arr)->list:
        model_arr = []
        for k in arr:
            print(cls.fromJson(k))
            model_arr.append(cls.fromJson(k))
        return model_arr

    @classmethod
    def foodListToJson(cls,arr)->list:
        json_arr = []
        for k in arr:
             json_arr.append(cls.toJson(k))
        return json_arr
    
    
 