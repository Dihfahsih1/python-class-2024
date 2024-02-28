class Vehicle:
    def printConsumption(self):
        print('none')
class MotorVehicle(Vehicle):
    def printConsumption(self):
        print('medium')
        
class Car(MotorVehicle):
    pass
car=Car()
car.printConsumption() 