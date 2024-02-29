from abc import ABC,abstractmethod

class Abstractclass(ABC):
    def print(self):
        print("Abstract class - Normal method")
        
    @abstractmethod
    def printabstract(self):
        print("Abstract class - Abstract method")


class Childclass(Abstractclass):
    def print(self):
        print("this is the child class")
child=Childclass()

child.print()



#example 2


class Join(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Naming(self):
        print(f"my name is  {self.name}")

    @abstractmethod
    def Aging(self):
        print(f"i am {self.age} years old")


P1=Join("Chris",61)


