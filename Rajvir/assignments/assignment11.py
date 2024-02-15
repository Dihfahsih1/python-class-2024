# what is polymorphism in oop ..
# it means, many words, making it have different stages or forms.. we can execute the same method of all classes.
# example 1 is for class only:

class Car2:
    def __init__(self,brand,model):
        self.brand= brand 
        self.model=model 

    def move(self):
        print("Drive")

class Boat:
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

    def move(self):
        print("sail!")

car1 = Car2("ford", "mustang")
boat_1= Boat("ibiza", "toouring 16")

for x in (car1, boat_1):
    x.move()

#example 2 this belongs to class inheritence 

class Vehicle:
    def __init__(self,brand,model):
        self.brand= brand
        self.model = model

    def move(self):
        print("move!!")

class Car3(Vehicle):
    pass 

class Plane(Vehicle):
    def move(self):
        print("fly")

car4 = Car3("FORD","MUSTANG")
plane1= Plane("Rajvir","456")

for x in (car4, plane1):
    print(x.brand)
    print(x.model)
    x.move()