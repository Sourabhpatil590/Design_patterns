from interface import Problem_Interface
from threading import Lock

class Optimized(Problem_Interface):
    __shared_instance = None
    __lock = Lock()

    def __new__(cls):
        if Optimized.__shared_instance == None:
            Optimized.__lock.acquire()
            if Optimized.__shared_instance == None:
                Optimized.__shared_instance = object.__new__(cls)
                Optimized.__lock.release()
                return Optimized.__shared_instance
        else:
            raise Exception('Singleton object ! Object is already created.')
            

    def rain_water_tapping(self):
        print('Rain water tapping problem solved by Optimized approach')
    
    @staticmethod
    def getinstance():
        if Optimized.__shared_instance == None:
            Optimized.__shared_instance = Optimized()
            return Optimized.__shared_instance
        else:
            return Optimized.__shared_instance