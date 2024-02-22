from abc import ABC, abstractmethod

class Vehical(ABC):

    @abstractmethod
    def model(self):
        print("This is an abstract class.")
        return

    def method1(self):
        print("This is a concrete method")

class Car(Vehical):
    def model(self):
        super().model
        return

car1 = Car()
car1.model()
car1.method1()