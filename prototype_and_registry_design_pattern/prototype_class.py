from clone_interface import Clone
# same fare, same train type, same engine type, same number of seats but have different timings, and stations

class Train(Clone):

    def __init__(self, obj = None) -> None:
        self.__fare = obj.fare if obj else None
        self.__engine_type = obj.engine_type if obj else None
        self.__seats = obj.seats if obj else None
        self.__timings = obj.timings if obj else None
        self.__stations = obj.stations if obj else None

    def clone(self):
        obj = Train(self)
        return obj

    def __str__(self) -> str:
        return f'station : {self.__stations}, timing : {self.__timings}.'

    def setfare(self, fare):
        self.__fare = fare

    def getfare(self):
        return self.__fare

    def setengine_type(self, engine_type):
        self.__engine_type = engine_type

    def getengine_type(self):
        return self.__engine_type

    def setseats(self, seats):
        self.__seats = seats

    def getseats(self):
        return self.__seats

    def settimings(self, timings):
        self.__timings = timings

    def gettimings(self):
        return self.__timings

    def setstations(self, stations):
        self.__stations = stations

    def getstations(self):
        return self.__stations