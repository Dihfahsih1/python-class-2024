from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def method1(self):
        print("This is an abstruct method")
        return 
    
class concreteclass(Student):
    def method1 (self):
        super().method1()
        return

obj = concreteclass()
obj.method1()