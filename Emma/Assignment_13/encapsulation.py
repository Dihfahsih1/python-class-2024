
  # Answer 1
class Dog:
    def __init__(self,name,age):
        self.name = name
        self._age = age

    def getName(self):
        print(f"its name is {self.name}")

    def getAge(self):
        print(f"its age is {self._age} years")


D = Dog("Spick",2)
D.getName()
D.getAge()


  #Answer 2

class Nuts:
    def __init__(self,name,breed):
        self.name = name
        self._breed = breed

    def getId(self):
        print(f"its ID is {self.name}")

    def getbreed(self):
        print(f"its breed is {self._breed} years")


D = Nuts("wallnut","norma")
D.getId()
D.getbreed()