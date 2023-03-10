# abstract class
from abc import ABC, abstractmethod

class vehicle(ABC):


# abstract Methos
    @abstractmethod
    def getValue(self):
        pass



class car(vehicle):

    def __init__(self,make,model,fare) -> None:
        super().__init__()
        self.make = make
        self.model = model
        self.fare = fare

    def getValue(self):
        return 100*self.fare
    


homecar = car("tesla", 2022, 40)
print(homecar.getValue())

