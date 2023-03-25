'''
Create a child class Bus, Car, Scooter that will inherit all of the variables and methods of the Vehicle class
'''

#Solution:
class Vehicle:
    def __init__(self, name, no_of_wheels, speed, mileage):
        self.no_of_wheels = no_of_wheels
        self.name = name
        self.speed = speed
        self.mileage = mileage
        
    def display(self):
        print("This is a "+self.name+", with "+self.no_of_wheels+" wheels, speed:"+self.speed+", and mileage:"+self.mileage)
        
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

class Scooter(Vehicle):
    pass

b = Bus("Bus","4", "180", "12")
b.display()

c = Car("Car","4", "220", "12")
c.display()

s = Scooter("Scooter","2", "120", "10")
s.display()
