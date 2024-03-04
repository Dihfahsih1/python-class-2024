from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):]
        return "Driving a car..."


class Motorcycle(Vehicle):
    def drive(self):
        return "Riding a motorcycle..."