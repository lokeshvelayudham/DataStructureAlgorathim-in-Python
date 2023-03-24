class vehicle():
    def __init__(self,make,model,fuel) -> None:
        self.make = make
        self.model = model
        self.fuel = fuel
        
    def getvalue(self):
        try:
            age = 2021 - self.model
            return 1000*(1/age)
        except TypeError:
            try:
                age = 2021 - int(self.model)
                return 1000*(1/age)
            except ZeroDivisionError:
                age = 2021 - int(self.model)
                return 1000*(1)


pscar = vehicle("tesla",2019,"ev")
hscar = vehicle("honda","2020","petrol")
bscar = vehicle("ford",'2021',"de")


print(pscar.getvalue())
print(hscar.getvalue())
print(bscar.getvalue())