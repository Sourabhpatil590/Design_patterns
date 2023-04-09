from icecream.icecream_interface import Icecream_Interface

class Chocolate_toppings(Icecream_Interface):
    def __init__(self, icecream) -> None:
        self.__cost = 5
        self._discription = ' Chocolate_toppings'
        self.obj = icecream
        self.__cost += self.obj.get_cost()
        self.__discription = self.obj.get_discription() + ',' + self.__discription

    def get_cost(self):
        return self.__cost

    def get_discription(self):
        return self.__discription