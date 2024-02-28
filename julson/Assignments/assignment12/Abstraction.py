# Abstraction in Python Object-Oriented Programming (OOP) is the concept of hiding the implementation details of a class and only showing the essential features of the object. 

# Abstraction helps in managing complexity, promoting code reusability, and providing a clear interface for interacting with objects.

from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def drive(self):
        return f"{self.make} {self.model} is driving."

    def stop(self):
        return f"{self.make} {self.model} has stopped."

class Motorcycle(Vehicle):
    def drive(self):
        return f"{self.make} {self.model} is riding."

    def stop(self):
        return f"{self.make} {self.model} has stopped."

# Usage
car = Car("Toyota", "Camry")
print(car.drive())  # Output: Toyota Camry is driving.
print(car.stop())   # Output: Toyota Camry has stopped.

motorcycle = Motorcycle("Harley-Davidson", "Sportster")
print(motorcycle.drive())  # Output: Harley-Davidson Sportster is riding.
print(motorcycle.stop())   # Output: Harley-Davidson Sportster has stopped.