from abc import ABC, abstractclassmethod

class AdapterInterface:

    @abstractclassmethod
    def createmeetinglink(self):
        pass

    @abstractclassmethod
    def add_participants(self):
        pass

    @abstractclassmethod
    def schedule(self):
        pass