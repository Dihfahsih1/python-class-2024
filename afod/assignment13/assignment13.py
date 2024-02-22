#Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different
#  classes to be treated as objects of a common superclass. It enables flexibility and extensibility in code by
#   allowing methods to be invoked on objects of different classes without knowing their specific types at
#    compile time
# 
#  abstract polorphism
class Language:
    def say_hello(self):
        raise  NotImplementedError("Please use say_hello class in child class")

class French(Language):
    def say_hello(self):
        print("Bonjuor")

class Chinese(Language):
    def say_hello(self):
        print("nia hao")

def intro(lang):
    lang.say_hello()

Naomi = French()
john = Chinese()

intro(Naomi)
intro(john)
# example2
#Run-Time Polymorphism (Method Overriding):In run-time polymorphism, a method in a subclass overrides 
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


#ABSTRACTION
    #This refers to the process of hiding the implementation details of a class and only showing the essential
# features of the project.
# it focuses on what the project does and not how it does.
# in python the way we achieve abstraction is by inheritence,abstract classes and interfaces
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Usage
circle = Circle(5)
rectangle = Rectangle(3, 4)
print(circle.area())      # Output: 78.5
print(rectangle.area())   # Output: 12


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius= radius

    def area(self):
        return 3.142*self.radius**2

    def perimeter(self):
        return 2*3.142*self.radius


class Triangle(Shape):
    def __init__(self, base, height, sides):
        self.base= base
        self.height= height
        self.sides= sides

    def area(self):
        return 0.5*self.base*self.height

    def perimeter(self):
        return sum(self.sides)


class Customer:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

# Using data abstraction to access customer information
customer1 = Customer("Alice", 30)
customer2 = Customer("Bob", 25)

print("Customer 1:", customer1.get_name(), customer1.get_age())  # Output: Customer 1: Alice 30
print("Customer 2:", customer2.get_name(), customer2.get_age())  # Output: Customer 2: Bob 25
