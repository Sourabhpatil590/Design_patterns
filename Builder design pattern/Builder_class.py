class Student(object):
    def __new__(cls, *args, **kwargs):
        dct = kwargs
        if dct:
            Student.validatename(dct['name'] if 'name' in dct else 'None')
            Student.validategradyear(dct['gradyear'] if 'gradyear' in dct else 0)
            Student.validateyoe(dct['yoe'] if 'yoe' in dct else 100)
        
        return object.__new__(cls)
        
    def __init__(self, *args, **kwargs) -> None:
        dct = kwargs
        self.__name = None
        self.__yoe = None
        self.__gradyear = None
        if len(dct) > 0:
            print('inside kwargs')
            self.__name = dct['name'] if 'name' in dct else 'None'
            self.__yoe = dct['yoe'] if 'yoe' in dct else 100
            self.__gradyear = dct['gradyear'] if 'gradyear' in dct else 0

    @staticmethod
    def validatename(name):
        if(name == None):
            raise Exception("Name is invalid")
        else:
            return True

    @staticmethod
    def validateyoe(exp):
        if exp < 1:
            raise Exception("Years of experience should be atleast 1")
        else: 
            return True

    @staticmethod
    def validategradyear(yr):
        if yr >= 2023:
            raise Exception("Grad year should be 2022 or earlier")
        else:
            return True


    def setname(self, name):
        Student.validatename(name)
        self.__name = name

    def getname(self):
        return self.__name

    def setyoe(self, exp):
        Student.validateyoe(exp)
        self.__yoe = exp

    def getyoe(self):
        return self.__yoe

    def setgradyear(self, yr):
        Student.validategradyear(yr)
        self.__gradyear = yr

    def getgradyear(self):
        return self.__gradyear

    

