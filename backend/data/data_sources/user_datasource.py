from .database_source import DatabaseSource
from ..Models.user_model import UserModel
from abc import ABC,abstractmethod




#User class handles the CRUD operations in database 
class UserDatasource(DatabaseSource):
   
    """Creates a singleton instance of the UserRepository class.
        This ensures that only one instance of the class is created
        and shared across the application.
        The __new__ method is overridden to control the instantiation
        process. If an instance already exists, it returns that instance."""

    # def __new__(cls):
    #     super(DatabaseSource).__init__()
    #     if not hasattr(cls,'user_instance'):
    #         if(cls._cursor is None):
    #             if(cls._conn is None):
    #                 cls.connect()                    
    #             cls._cursor = cls._conn.cursor()
    #         cls.user_instance = super(UserDatasource,cls).__new__(cls)
    #     return cls.user_instance 
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()


    #inserting the user data into the database
    def createUser(self,json_data)->int:
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
        

        


