class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.is_running= False

    def start_engine(self):
        self.is_running= True
        print("The engine is running..")

    def stop_engine(self):
        self.is_running= False
        print("The engine has stopped..")


make=input("The car Make: ")
model=input("The car Model:")
year=int(input("The car year:"))

my_car=Car(make, model, year)
print(f"The car make is {my_car.make}")
print(f"The car model is {my_car.model}") 
print(f"The car year is {my_car.year}")

#Inheriting from class Car above   
class Vehical(Car):
    pass              #we pass because we dont want any methods under this new(inherited) class

my_car2= Vehical('Toyota', 'T20', 2020)
print(my_car2.make)
print(my_car2.model)
print(my_car2.year)
