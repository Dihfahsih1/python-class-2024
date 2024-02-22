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
#Encapsulation helps impelement on private and public variables using either single underscore or double underscore

#Example 1
class Student:

    def __init__(self, name, marks):
        self.__name=name            #this double underscore makes name a private variable
        self.__marks=marks

class Student_profile(Student):

    def Student_data(self):
        print(f"The student name is {self.__name} with {self.__marks} marks")

student1= Student("John", 91)
    

#Example 2 
class Employee:

    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def employee_data(self):
        print("This is the Employee's private data")


class Employee_info(Employee):
    def employee_data(self):
        print("This is the Employee's private data")

employee1= Employee("David", 30)
employee2= Employee("Sarah", 40)

# print(employee1.name)            #this wont print because name and age is private in the employee parent class
# print(employee2.age)


