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
