class UserModel:
    def __init__(self,name:str = None,age:int = None,height:float=None,weight:float=None,phone:int = None,gender:str = None):
        self.id = None
        self.name:str = name
        self.age:int = age
        self.height:float = height
        self.weight:float = weight
        self.phone:int = phone
        self.gender:str = gender

    def toDataBase(self,json_data):
        user = self.fromJson(json_data)
        return(3434,user.name,user.phone,user.age,user.weight,user.gender)
    
    @classmethod
    def fromJson(user,json_data):
        return user(
            name=json_data["name"],
            age=json_data["age"],
            height = json_data["height"],
            weight = json_data["weight"],
            phone = json_data["phone"],
            gender = json_data["gender"]
            
            )
    

    

