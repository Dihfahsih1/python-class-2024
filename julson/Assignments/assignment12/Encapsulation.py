# Encapsulation in Python refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, known as a class. It allows for data hiding, meaning that the internal state of an object can only be accessed and modified through the object's methods, thus providing control over how data is accessed and manipulated. This helps in keeping the code modular, organized, and easier to maintain.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = 0  # Private attribute

    def get_odometer_reading(self):
        return self.__odometer_reading

    def update_odometer(self, mileage):
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.__odometer_reading += miles


my_car = Car("Toyota", "Camry", 2022)
print(my_car.get_odometer_reading())  # Output: 0
my_car.update_odometer(100)
print(my_car.get_odometer_reading())  # Output: 100