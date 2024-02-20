#Abstarction #This is a method of exposing relevant data and hiding other data. for example in example 1 the abstracted class Vehical acts as a blueprint to other classes

from abc import ABC, abstractmethod              #abc is a module that helps achieve abstraction

#Example 1
class Vehical(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehical):
    def start(self):
        print("Start the engine.")

class Bike(Vehical):
    def start(self):
        print("Start peddling")

car1=Car()
car1.start()

car2=Bike()
car2.start()

print("----------------------------------")
# Example 2

class Computer(ABC):

    def __init__(self, model_1,model_2):
        self.model_1=model_1
        self.model_2=model_2

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("It is running")

class Phone(Computer):
    def process(self):
        print("It is working")

model_1=input("Enter the laptop model name: ")
model_2=input("Enter the phone model name: ")

comp1=Laptop(model_1,model_2)
print(f"The laptop model is {comp1.model_1}")
comp1.process()

comp2=Phone(model_1,model_2)
print(f"The phone model is {comp2.model_2}")
comp2.process()

print("----------------------------------")

#Encapsulation
#Encapsulation helps impelement on private and public variables using either single underscore or double underscore

class Student:

    def __init__(self, name, marks):
        self.__name=name            #this double underscore makes name a private variable
        self.__marks=marks

    def Student_data(self):
        print(f"The name of student is {self.__name} and the marks are {self.__marks}")

student1= Student("Paul", 20)
student1.Student_data()

student2= Student("Maya", 91)
student2.Student_data()