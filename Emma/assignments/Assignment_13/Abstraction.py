from abc import ABC,abstractmethod

# abstraction refers to the process of hiding complex implementation details and showing only the essential features of an object
   # answer  1
class Trousers(ABC):
    def __init__(self,name,size):
        self.name = name
        self.size = size
    @abstractmethod
    def Name(self):
        print(f"This trouser is called a {self.name}")

    
    def Size(self):
        print(f"Its size is {self.size}")

class Cargo_trous(Trousers):
    def __init__(self, name, size):
        super().__init__(name, size)

    def Name(self):
        super().Name()
      

    
    def Size(self):
        print(f"Its size is {self.size}")

    # def cargo_name(self):
    #     super().Name()


T = Cargo_trous("Plain cargoes",34)
T.Name()
T.Size()


  #Answer 2


class Phone(ABC):
    def __init__(self,model,price):
        self.model=model
        self.price=price
        
    @abstractmethod
    def Mod_print(self):
        print(f"its model is {self.model}")
        return

    def price_print(self):
        print(f"its price is {self.price} USD")
        return


class Iphones(Phone):
    def Mod_print(self):
        super().Mod_print()
        return


#I15 = Iphones("I15",1200)
#I15.Mod_print()


        

        