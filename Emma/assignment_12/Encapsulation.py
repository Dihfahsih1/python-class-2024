
#example 1
class Person:
    name="Code as it is "
    def __init__(self):
        self.age=35
        self.__salary=1000

class employee(Person):
    def __init__(self):
        super().__init__()
        print(self.age)
        print(self.__salary)


employee()


#example 2

class Fruits():
    def __init__(self,name,type):
        self.name="Greg"
        self.__type=7

    def namig(self):
        print(self.name)

    def type(self):
        print(self.__type)


class mango(Fruits):
    def __init__():
        super().__init__()
        
    






