from interface import Problem_Interface
from threading import Lock

class Bruteforce(Problem_Interface):
    __shared_instance = None
    __lock = Lock()

    def __new__(cls):
        if Bruteforce.__shared_instance == None:
            Bruteforce.__lock.acquire()
            if Bruteforce.__shared_instance == None:
                Bruteforce.__shared_instance = object.__new__(cls)
                Bruteforce.__lock.release()
            return Bruteforce.__shared_instance
        else:
            raise Exception('Singleton object ! Object is already created.')
        

    def rain_water_tapping(self):
        print('Rain water tapping problem solved by Bruteforce approach')
    
    def getinstance(cls):
        if Bruteforce.__shared_instance == None:
            Bruteforce.__shared_instance = Bruteforce()
            return Bruteforce.__shared_instance
        else:
            return Bruteforce.__shared_instance