from .db import DataBase
from Models.user_model import UserModel


class User(DataBase):
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()

    def signIn(self,json_data):
        
        user = UserModel().toDataBase(json_data=json_data)
        self._cursor.execute("INSERT INTO Users VALUES(?,?,?,?,?,?)",user)
        self._conn.commit()

    def getUser(self,field,value):
        query = f"SELECT * FROM Users WHERE {field}={value}";
        self._cursor.execute(query)
        users = self._cursor.fetchone()
        print(users)
        return users

