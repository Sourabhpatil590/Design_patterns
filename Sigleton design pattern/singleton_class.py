class singleton(object):
    __obj = None

    def __new__(cls, *args):
        if singleton.__obj == None:
            # singleton.__status = 'created'
            return object.__new__(cls)
        else:
            raise Exception ('object cant be created')
        
    def __init__(self, *args) -> None:
        if args:
            name = args
            self.name = name[0]
            print(self.name)
        singleton.__obj = self
        

    def __str__(self) -> str:
        return str(id(self))
            
    @staticmethod
    def getInstance():
        if singleton.__obj == None:
            singleton()
            return singleton.__obj
        else:
            return singleton.__obj
            