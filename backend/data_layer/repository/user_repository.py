from .db import DataBase
from ..Models.user_model import UserModel
from abc import ABC,abstractmethod

class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def signIn(self,json_data):
        pass

    @abstractmethod
    def getUser(self,field,value):
        pass



#User class handles the CRUD operations in database 
class UserRepository(DataBase,UserRepositoryInterface):
    _cursor = None
    
    def __new__(cls):
        super(DataBase).__init__()
        if not hasattr(cls,'user_instance'):
            if(cls._cursor is None):
                if(cls._conn is None):
                    cls.connect()                    
                cls._cursor = cls._conn.cursor()
            cls.user_instance = super(UserRepository,cls).__new__(cls)
        return cls.user_instance 
    
    # def __init__(self):
    #     # super().__init__() #initializing the parent class
    #     self._cursor = self._conn.cursor()


    def signIn(self,json_data):
        userModel = UserModel()

        # user = userModel.toDatabase(json_data=json_data)
        user2 = userModel.jsonToTuple(json_data)

        # temp = list(user)
   
        # temp.append(json_data["pwd"])
        # user_with_pwd = tuple(temp) 

        self._cursor.execute(f"INSERT INTO Users{user2.columns} VALUES{user2.values}") #Inserting rows into the User table
        id = self._cursor.lastrowid
        
        # print(id)
        self._conn.commit()
        # self.close()
        return id

    def getUser(self,field,value):
        query = 'SELECT * FROM Users WHERE {}=\'{}\''.format(field,value)
        self._cursor.execute(query)
        users = self._cursor.fetchone()
        return users
    
    def updateUser(self,json_data,id):
        model = UserModel.jsonToUpdate(json_data=json_data,id=id)
        self._cursor.execute(f"UPDATE {model.columns}",model.values)
        

        


