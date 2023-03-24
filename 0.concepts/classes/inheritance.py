# Parent class
class vehicle:
    # instance method 
    def __init__(self,make,model,fuel):
        # instace Attribute
        # public Attribute
        self.make = make

        # private Attribute
        self.__model = model
        self.__fuel = fuel
    
    # private instance method
    def __private_method_parent(self):
        print("private method in parent class")


# child class
class car(vehicle):
    # instance method
    def __init__(self, make, model, fuel,sunroof,ac):
        super().__init__(make, model, fuel)

        self.sunroof = sunroof
        self.ac = ac


# object
personalcar = car("tesla",2022,"ev",True,True)

# public child class call
print(personalcar.__dict__)

# parent private instance 
print(personalcar._vehicle__private_method_parent())
