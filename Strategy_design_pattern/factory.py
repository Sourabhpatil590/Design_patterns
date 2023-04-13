from bruteforce import Bruteforce
from average import Average
from optimized import Optimized
from approaches import Approaches

class Factory:

    def select_method(self, approach):
        if approach == Approaches.Bruteforce.name:
            return Bruteforce()
        elif approach == Approaches.Average.name:
            return Average()
        elif approach == Approaches.Optimized.name:
            return Optimized()
