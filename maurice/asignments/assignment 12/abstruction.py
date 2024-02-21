# abstraction is used to to hide the irrelevant data to reduce complexity
from abc import ABC
class Car(ABC):
    def Toyota(self):
        pass
class Tesla(Car):
    def Toyota(self):
        print("Toyota is slowing down")
class Suzuki(Car):
    def Toyota(self):
        print("Toyota is stopping")
class BMW(Car):
    def Toyota(self):
        print("Toyota has stopped")
c1=Tesla()
c1.Toyota()
c2=Suzuki()
c2.Toyota()
c3=BMW()
c3.Toyota()
