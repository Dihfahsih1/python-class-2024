from abc import ABC,abstractmethod
from math import sqrt


class squareroot(ABC):
    def __init__(self,st):
        self.st = st
    

    
    @abstractmethod
    def squareroot(self):
        print(f"The square root of {self.st} is {sqrt(self.st)}")


class root(squareroot):

    def squareroot(self):
        return super().squareroot()
user_input = int(input("enter the negative number whose squareroot you want to find : "))
sqrtd = root(user_input*-1)
sqrtd.squareroot()

        