from .mapper import MapperInterface
from ...domain.entities.food_entitie import FoodEntitie

class FoodMapper(FoodEntitie,MapperInterface):
    def __init__(self,id:str = None,name:str = None,energy:float= None,calorie:float=None,protien:float = None):
        super().__init__(
              id=id,
              name = name,
              energy=energy,
              calorie=calorie,
              protien=protien
        )
        
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
    
