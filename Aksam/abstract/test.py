from abc import abstractmethod

from class_1 import ABC

class Human(ABC):
    def __init__(self, name, size):
        self.name = name
        self.sized = size
        
    @abstractmethod
    def method1(self):
        print("Hello world")
    
    def method2(self):
        print("Hello world guys")
    
    
class MorgCity(Human):
    def method1(self):
        super().method1()
        return
    
city = MorgCity("Aksam", 40)
city.method1()
city.method2()
