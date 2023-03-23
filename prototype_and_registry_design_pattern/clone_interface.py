from abc import ABC, abstractclassmethod

class Clone(ABC):
    @abstractclassmethod
    def clone():
        pass