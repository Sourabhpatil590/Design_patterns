from interface import Problem_Interface
from threading import Lock

class Average(Problem_Interface):
    __shared_instance = None
    __lock = Lock()

    def __new__(cls):
        if Average.__shared_instance == None:
            Average.__lock.acquire()
            if Average.__shared_instance == None:
                Average.__shared_instance = object.__new__(cls)
                Average.__lock.release()
                return Average.__shared_instance
        else:
            raise Exception('Singleton object ! Object is already created.')
        

    def rain_water_tapping(self):
        print('Rain water tapping problem solved by Average approach')
    
    def getinstance(cls):
        if Average.__shared_instance == None:
            Average.__shared_instance = Average()
            return Average.__shared_instance
        else:
            return Average.__shared_instance