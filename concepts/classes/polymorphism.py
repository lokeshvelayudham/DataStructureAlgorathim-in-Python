# Parent class
class vehicle:

    currentYear = 2023
    basePrice = 1000

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
    
    # default function to get value of the car
    def getValue(self):
        age = vehicle.currentYear-self.__model
        print("This is default method of parent")
        return vehicle.basePrice*(1/age)



# child class
class car(vehicle):
    # instance method
    def __init__(self, make, model, fuel,sunroof,ac):
        super().__init__(make, model, fuel)

        self.sunroof = sunroof
        self.ac = ac
    # overrideing the method replace the parent defult method
    def getValue(self):
        vehicle.basePrice = 5000
        age = vehicle.currentYear-self._vehicle__model
        print("This is childs override")
        return vehicle.basePrice*(1/age)

# object
personalcar = car("tesla",2019,"ev",True,True)

# public child class call
print(personalcar.__dict__)

# parent private instance 
print(personalcar._vehicle__private_method_parent())

# polymorphism
print(personalcar.getValue())

