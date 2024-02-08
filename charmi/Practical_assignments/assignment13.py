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

#Encapsulation

#Example 1
class Student:

    def __init__(self, name, marks):
        self.__name=name            #this double underscore makes name a private variable
        self.__marks=marks

    def Student_data(self):
        print(f"The name of student is {self.__name} and the marks are {self.__marks}")

student1= Student("Paul", 20)
student1.Student_data()

#Example 2 
class Employee:

    def __init__(self,name,age):
        self._name=name
        self._age=age

    def employee_data(self):
        print("This is the Employee's private data")

employee1= Employee("David", 30)
employee2= Employee("Sarah", 40)

print(employee1._name)
print(employee1._age)

print(employee2._name)
print(employee2._age)


