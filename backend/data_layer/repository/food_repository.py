from .db import DatabaseRepository
from .jaro import JaroWrinklerSearching
from ..Models.food_model import FoodModel
from abc import ABC,abstractmethod
from ..Models.food_model import FoodModel
from .irepositories.ifood_repository import FoodRepositoryInterface


# class FoodRepositoryInterface(ABC):
#     @abstractmethod
#     def getData(self):
#         pass
#     @abstractmethod
#     def searchFood(self,query):
#         pass

#     @abstractmethod
#     def updateFoodField(self,json_data):
#         pass

class FoodRepository(FoodRepositoryInterface,DatabaseRepository,):
    """Creates a singleton instance of the FoodRepository class.
        This ensures that only one instance of the class is created
        and shared across the application.
        The __new__ method is overridden to control the instantiation
        process. If an instance already exists, it returns that instance."""

    def __new__(cls):
        if not hasattr(cls,"food_instance"):
            cls.food_instance = super(FoodRepository,cls).__new__(cls)
        return cls.food_instance
    
    #Constructor of the FoodRepository class
    #It initializes the cursor and connection to the database
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()
      
    # retrieves the food data from the database
    def getData(self):
        datas = []
        task = "SELECT * FROM Foods"
        self._cursor.execute(task)
        data = self._cursor.fetchall()
        for i in data:
            model:FoodModel = FoodModel.fromJson(i)
            model.name = str(model.name[0])     
            datas.append(model)

        return datas
    

    #jarowinkler searching
    def searchFood(self,query,db_data):
        # send_data = self.getData()
        datas = []
        # print(db_data)
        for i in db_data:
            # print(i)
            datas.append(FoodModel.fromJson(i))
        jaro_search = JaroWrinklerSearching(datas)
        sorted_list = jaro_search.hybrid_search(query=query)
        arr = []
        for data in sorted_list:
            arr.append(data.toJson())

        return arr

    #updates the food data in the user table 

    def updateFoodField(self,json_data):
        model = FoodModel.jsonToUpdate(json_data = json_data,query_value=json_data.get("id"))   #json to updating format
        task = f"UPDATE Users SET {model.columns} WHERE id=?"
        self._cursor.execute(task,model.values) #execute query
        self._conn.commit() #update the database
    
    def knapsack_food(self,json_data,calorie):
        foods = FoodModel.listMaptoFood(json_data)

        for k in  foods:
            print(f"{k.calorie},{k.protien}")
        foods.sort(key=lambda x:(x.protien/x.calorie),reverse=True)
        finalCalorie = 0.0
        addedFoods = []
        
        for food in foods:
            if(food.calorie <= calorie):
                finalCalorie += food.calorie
                calorie -= food.calorie
                addedFoods.append(food)
            else:
                food_model = food
                finalCalorie += calorie
                food_model.calorie = calorie
                food_model.protien = food.protien*calorie/food.calorie
                
                addedFoods.append(food_model)
                break
        print(calorie)
        return FoodModel.foodListToJson(addedFoods)