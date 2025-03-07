from .db import DataBase
from ..Models.user_model import UserModel

#User class handles the CRUD operations in database 
class UserRepository(DataBase):
    def __init__(self):
        super().__init__() #initializing the parent class
        self._cursor = self._conn.cursor()


    def signIn(self,json_data):
        
        user = UserModel().toDatabase(json_data=json_data)
        temp = list(user)
   
        temp.append(json_data["pwd"])
        user_with_pwd = tuple(temp) 
     
        self._cursor.execute("INSERT INTO Users (id,name,email,pwd) VALUES(?,?,?,?)",user_with_pwd) #Inserting rows into the User table
        self._conn.commit()
        self.close()

    def getUser(self,field,value):
        query = 'SELECT * FROM Users WHERE {}=\'{}\''.format(field,value)
        self._cursor.execute(query)
        users = self._cursor.fetchone()
        return users
    

        


