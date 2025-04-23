from .db import DatabaseRepository
from ..Models.user_model import UserModel
from abc import ABC,abstractmethod


#Blueprint of the UserRepository class
class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def signIn(self,json_data):
        pass

    @abstractmethod
    def getUser(self,field,value):
        pass



#User class handles the CRUD operations in database 
class UserRepository(DatabaseRepository,UserRepositoryInterface):
    _cursor = None
    
    """Creates a singleton instance of the UserRepository class.
        This ensures that only one instance of the class is created
        and shared across the application.
        The __new__ method is overridden to control the instantiation
        process. If an instance already exists, it returns that instance."""

    def __new__(cls):
        super(DatabaseRepository).__init__()
        if not hasattr(cls,'user_instance'):
            if(cls._cursor is None):
                if(cls._conn is None):
                    cls.connect()                    
                cls._cursor = cls._conn.cursor()
            #object class is responsible for object creating and initialization
            cls.user_instance = super(UserRepository,cls).__new__(cls)
        return cls.user_instance 


    #inserting the user data into the database
    def signIn(self,json_data):
        userModel = UserModel()
      
        user2 = userModel.jsonToTuple(json_data) #json to tuple
        self._cursor.execute(f"INSERT INTO Users{user2.columns} VALUES{user2.values}") #Inserting rows into the User table
        id = self._cursor.lastrowid #returns the id of created user
        self._conn.commit() #update the database
        return id

    #retrieves the user data from the database
    def getUser(self,field,value):
        query = 'SELECT * FROM Users WHERE {}=\'{}\''.format(field,value)
        self._cursor.execute(query) 
        users = self._cursor.fetchone()
        return users
    
    #updates the user data in the database
    def updateUser(self,json_data,id):
        model = UserModel.jsonToUpdate(json_data=json_data,id=id)
        self._cursor.execute(f"UPDATE {model.columns}",model.values)
        

        


