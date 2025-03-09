from abc import ABC,abstractmethod

class TupleConversion:
    def __init__(self,columns,values):
        self.columns =  columns
        self.values= values


class ModelInterface(ABC):

    @classmethod
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

    def jsonToTuple(self,json_data):
        keys = []
        values = []
        for k in json_data.keys():
            keys.append(k)
            values.append(json_data[k])
        keys = str(tuple(keys))
        values = str(tuple(values))
        return TupleConversion(values=values,columns=keys)



















































































    