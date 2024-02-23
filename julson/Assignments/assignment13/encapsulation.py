# Encapsulation is the concept of hiding the internal details of an object from the outside world

class Car:
    def __init__(self):
        self.__speed = 10   # Private variable
    
    def accelerate(self, increment):
        self.__speed += increment
    
    def get_speed(self):
        return self.__speed

car = Car()
car.accelerate(20)
print(car.get_speed())  # Output: 20