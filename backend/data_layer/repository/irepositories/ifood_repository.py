from abc import ABC,abstractmethod


class FoodRepositoryInterface(ABC):
    @abstractmethod
    def searchFood(self):
        pass