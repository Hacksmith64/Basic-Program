class Car:
    Wheels = 4
    def __init__(self):
        self.milege = 10
        self.Company = "BMW"

c1 = Car()
c2 = Car()
c1.milege = 30
Car.Wheels = 5
print(c1.Company,c1.milege,c1.Wheels)
print(c2.Company,c2.milege,c2.Wheels)