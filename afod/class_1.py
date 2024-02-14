class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.is_running=False
        
    def start_engine(self):
        self.is_running=True
        print("the engine has started")
        
        
    def stop_engine(self):
        self.is_running=False
        print("engine has been stopped")

make=input("Enter the Car Make: ")
model=input("Enter the Car model: ")  
year=int(input("Enter the Car Year: "))  
age=20 
      
my_car = Car(make, model, year)
   
print(f"The car Make: {my_car.make}")
print(f"The car Model: {my_car.model}")
print(f"The car Year: {my_car.year}")
my_car.start_engine()
print(my_car.is_running)

my_car.stop_engine()
print(my_car.is_running)