from abc import ABC, abstractclassmethod

class Icecream_Interface(ABC):

    # def add_cost(self, cost):
    #     self.__cost += cost

    # def add_discription(self, desc):
    #     self.__discription += desc

    # def get_cost(self):
    #     return self.__cost

    # def get_discription(self):
    #     return self.__discription

    @abstractclassmethod
    def get_cost():
        pass

    @abstractclassmethod
    def get_discription():
        pass 
