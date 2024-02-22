#from the class u created use it to inherit
#Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (subclass
#  or derived class) to inherit attributes and methods from an existing class (superclass or base class).

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "model S",2023, 100)
my_electric_car.display_info()

# how do we access a project/repository and create branches in it?
1. #you clone the repository
2.#then you navigate o the repositorydirectory
3.#then you reate a new branch using the comand -b new-"name of the new branch"


# what is polymorphism and give two examoles


# Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different
#  classes to be treated as objects of a common superclass. It enables flexibility and extensibility in code by
#   allowing methods to be invoked on objects of different classes without knowing their specific types at
#    compile time

#there are two types of polymorhismi.e
1.#Compile-Time Polymorphism (Method Overloading):multiple methods with the same name but different 
# parameters are defined within the same class. 
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Creating an instance of Calculator
calc = Calculator()

# Polymorphic method call
print(calc.add(2, 3, 4))  

2.#Run-Time Polymorphism (Method Overriding):In run-time polymorphism, a method in a subclass overrides 
# the implementation of a method with the same name and signature in its superclass.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Polymorphic method call
dog.speak()  
cat.speak()  
