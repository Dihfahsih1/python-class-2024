class Car:
    def __init__(self,name,make,year):
        self.name=name
        self.make=make
        self.year=year
    def description(self):
       print (f'Car_name: {self.name}, car_make: {self.make}, Year: {self.year}')
# inheritence
class Type(Car):
    pass
car_1=Type("mazda", 2021 ,2021)
car_1.description()
# HOW TO CREATE A BRANCH ON GITHUB
# Nvigate the main page of the repository.
# Click the View all branches option from the branch drop down menufrom the file view tree on the left
# Click on New branch
# Enter the branch Name 
# Choose a source for your branch
# Click Create branch
