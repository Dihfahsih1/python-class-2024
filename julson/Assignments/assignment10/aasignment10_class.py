class car:
    def __init__(self,name, model,year):
        self.Name=name
        self.Modal=model
        self.Year=year

    def is_running(self):
        Start_ingine=True
        print('The engine has sarted')

    def stop_running(self):
        print('The ingine has Stopped')
        stop_ingine=False

N = input("Car name :")
M = input("car model :")
Y = int(input("car Year"))

car1=car(N,M,Y)
car1.stop_running()