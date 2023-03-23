class Train_Prototype_Registry:
    def __init__(self) -> None:
        self.__dct = dict()

    def save(self, prototype):
        # print('prototype timings', prototype.gettimings() )
        self.__dct[prototype.gettimings()] = prototype

    def get(self, timing):
        return self.__dct[timing]