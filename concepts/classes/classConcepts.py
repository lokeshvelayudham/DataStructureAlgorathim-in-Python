# class
class student:
    # calss attribute 
    version = 0.01 

# instance Method
    def __init__(self,name,age) :
        # instance/object Attribute
        #public Attribute
        self.name = name

        # Private Attribute
        self.__age = age
# instance Method 
    def printobj(self):
        print(self.name,end = " ")
        print(self.__age)
# instance Method 
#private Method
    def __details(self):
        print("the age of "+ self.name + " is ", self.age)

# Static Method
    @staticmethod
    def place(city):
        print(city) 

# Factory method / Class Method
    @classmethod
    def beauty(cls,entry:str):
        name, age = entry.split(" ")
        return student(name.capitalize(),
                       age
                       )


# Main


# object1 created
s1 = student("lokesh",25)
print(s1.name)
print(s1.version)
# object call 
s1.printobj()
# s1.details()
s1.place("chennai")


# object2 created 
s2 = student("yamks",24)
# object call 
s2.printobj()
# s2.details()


# object3 created
ClassObject = student.beauty("lokesh 25")
print(ClassObject.__dict__)


# calling private attribute
print(s1._student__age)
