class FoodEntitie():
    def __init__(self,id:str = None,name:str = None,energy:float= None,calorie:float=None,protien:float = None):
        #instance variables
        self.id:int = id
        self.name:str = name,
        self.energy:float = energy
        self.calorie:float = calorie,
        self.protien:float = protien,
        self.similarity:int = None

