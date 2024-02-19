from abc import ABC, abstractmethod


class Solution(ABC):
    def __init__(self):
        print("Constructor")
        
    @abstractmethod
    def method1(self):
        print("This is an abstructed method")
 
class ConcreteSolution(Solution):
    def method1(self):
        return super().method1()
            
obj1=ConcreteSolution()