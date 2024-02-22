print("EXAMPLE1")
class Humans:
    def breathe(self):
        print("Humans can breathe")
    def speake(self):
        print("Humans can speake")
class Animals:
    def breathe(self):
        print("Animals can breathe")
    def speake(self):
        print("Animals cannot speake")
obj_hum=Humans()
obj_ani=Animals()
for object in (obj_hum, obj_ani):
    object.breathe()
    object.speake()

print("EXAMPLE2")
class Toyota:
    def Engine(self):
        print("A Toyota has an amazing engine")
    def speed(self):
        print("A Toyota is very fast")
class BMW:
    def Engine(self):
        print("A BMW has has a fairly nice engine")
    def speed(self):
        print("A BMW is super fast")
objects=[Toyota(),BMW()]
for object in objects:
    object.Engine()
    object.speed()

print("EXAMPLE3")
from abc import ABC, abstractmethod
class Weight_loss(ABC):
    @abstractmethod
    def work_out(self):
        "Abstract method"
        return
    
class Push_ups(Weight_loss):
    def work_out(self):
        super().work_out()
        print("Do 30 push-ups")
        return
    
class Sit_ups(Weight_loss):
    def work_out(self):
        super().work_out()
        print("Do 40 sit-ups")
        return
exercises=[Push_ups(),Sit_ups()]
for exercise in exercises:
    exercise.work_out()