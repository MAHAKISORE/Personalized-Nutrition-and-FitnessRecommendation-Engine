from .db import DataBase
from ..Models.user_model import UserModel


class User(DataBase):
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()

    def signIn(self,json_data):
        
        user = UserModel().toDataBase(json_data=json_data)
        temp = list(user)
   
        temp.append(json_data["pwd"])
        user_with_pwd = tuple(temp)
     
        self._cursor.execute("INSERT INTO Users VALUES(?,?,?,?,?,?,?)",user_with_pwd)
        self._conn.commit()

    def getUser(self,field,value):
        query = 'SELECT * FROM Users WHERE {}=\'{}\''.format(field,value)
        self._cursor.execute(query)
        users = self._cursor.fetchone()
        print(users)
        return users
    
    def login(self,json_data):
        email = json_data["email"]
        pwd = json_data["pwd"]

        user = self.getUser("email",email)
        if(user == None):
            return "Email has not been registered yet"
        
        if(user[6] == pwd):
            return "User verified"
        else:
            return "Wrong pwd"
        


