#Polymorphism - Having one method in many forms in different classes

# 'Example one'

class Vehical:
    def __init__(self, model, year):
        self.model=model
        self.year=year

    def move(self):
        print("The vehical is moving!")

class Bus(Vehical):
    def move(self):
        print("Driving!")

class Bike(Vehical):
    def move(self):
        print("Peddle!")

bus1=Bus("MiniBus", 2019) 
bike1=Bike("E-bike", 2020)
print("The bus model is: ", bus1.model)
print("The bike model is: ", bike1.model)

print("*"*20)

#Example 2

class Shape:
    def __init__(self, type, size):
        self.type= type
        self.size= size

    def draw(self):
        print("Draw")

class Circle(Shape):
    def draw(self):
        print("Draw the circle.")

class Square(Shape):
    def draw(self):
        print("Draw the sqaure.")

shape1=Circle("Circle", "small")
shape2=Square("Square", "big")

print(shape1.type)
print(shape2.type)

