from abc import ABC,abstractmethod

#converting json data to tuples for inserting the data in tables(SQLite3)
class TupleConversion:
    def __init__(self,columns,values):
        self.columns =  columns
        self.values= values

#Standard Blueprint for all models
class ModelInterface(ABC):

    @classmethod #method that returns the class itself
    @abstractmethod
    def fromJson(self,data):
        pass

    # @classmethod
    # @abstractmethod
    # def fromDatabase(self,data):
    #     pass
    

    @abstractmethod
    def toDatabase(self,json_data):
        pass
    
    #genralising for converting json data to tuple 
    def jsonToTuple(self,json_data):
        keys = []
        values = []
        for k in json_data.keys():#seperating keys and columns
            keys.append(k)  
            values.append(json_data[k])

        keys = str(tuple(keys))
        values = str(tuple(values))
        return TupleConversion(values=values,columns=keys)



















































































    