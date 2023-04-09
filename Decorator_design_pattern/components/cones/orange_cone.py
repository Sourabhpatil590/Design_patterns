from icecream.icecream_interface import Icecream_Interface

class Orange_Cone(Icecream_Interface):
    def __init__(self, icecream=None):
        self.__cost = 15
        self.__discription = ' Orange Cone'
        self.obj = icecream

        if self.obj != None:
            self.__cost += self.obj.get_cost()
            self.__discription = self.obj.get_discription() + ',' + self.__discription

    def get_cost(self):
        return self.__cost

    def get_discription(self):
        return self.__discription
