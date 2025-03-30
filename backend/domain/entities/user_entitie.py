import re

class UserEntitie():
    def __init__(self,id:int = None,name:str = None,email:str = None,height:float=None,age:int = None,weight:float = None,bmi:float = None,allergy:int = None,diabetes:int=None,hyper_tension:int=None,gender:str = None):
        self.id:int = id
        self.name:str = name
        self.email:str = email
        self.height:float = height
        self.weight:float = weight
        self.age:int = age
        self.bmi:float = bmi
        self.allergy:int = allergy
        self.diabetes:int = diabetes
        self.hyper_tension:int = hyper_tension
        self.gender:str = gender
      

    def emailValid(self)->bool:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if(self.email == None or not re.fullmatch(regex,self.email)):
            return False
        return True
    
    

