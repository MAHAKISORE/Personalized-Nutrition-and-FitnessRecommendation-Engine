from ..Models.health_model import HealthModel
from abc import ABC,abstractmethod
from .user_datasource import UserDatasource
from .database_source import DatabaseSource

     

class HealthDatasource(DatabaseSource):

    """Creates a singleton instance of the HealthRepository class.
        This ensures that only one instance of the class is created
        and shared across the application.
        The __new__ method is overridden to control the instantiation
        process. If an instance already exists, it returns that instance."""
    _cursor = None
    def __new__(cls):
    
        if not hasattr(cls,'health_instance'):
            cls.health_instance =  super(HealthDatasource,cls).__new__(cls)
        if cls._cursor == None:
             cls._cursor = cls._conn.cursor()        
        return cls.health_instance
    
    #Constructor of the HealthRepository class
    #It initializes the cursor and connection to the database
    def __init__(self):
        super().__init__()
    
    #calculates the BMI of the user
    #BMI = weight(kg)/height(m)^2
    def bmi(self,height,weight):
        return weight/(height*height)
    
    def updateHealthFields(self,json_data):
            updates = HealthModel.jsonToUpdate(json_data=json_data,query_value=json_data["id"]) #json to updating format
            print(f"UPDATE Users SET {updates.columns} WHERE id=?",updates.values)  #update query
            self._cursor.execute(f"UPDATE Users SET {updates.columns} WHERE id=?",updates.values)   #exceute query
            self._conn.commit() #update the database
       
        
             
        


