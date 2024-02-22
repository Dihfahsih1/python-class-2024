print("EXAMPLE 1")
# Encapsulation refers to creating a shield that that prevents data from being accessed by the code outside the shield
# IT MAKES VARIABLES INACCESSIBLE IF CALLED OUUTSIDE THE THE CLASS 
# BUT THE SHIELDED VARIABLE CAN BE ACCESSED USING A TECHNIQUE CALLED 'NAME MANGLING"i.e obj.__class__varible
class Workers:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    def workerd_data(self):
        print(f'Name:{self.__name},Salary:{self.__salary}')
w1=Workers("Mercy",30)
w2=Workers("Fred",32)
w1.workerd_data()
w2.workerd_data()

print("EXAMPLE2")
class Laptops:
    def __init__(self,type,year):
        self.__type=type
        self.__year=year
    def laptop_data(self):
        print(f'Name:{self.__type},Salary:{self.__year}')
l1=Laptops("Toshiba",1994)
l2=Laptops("Fred",32)
l1.laptop_data()
l2.laptop_data()

print("EXAMPLE 3")
class Music:
    def __init__(self,genre,musician):
        self.__genre=genre
        self.__musician=musician
    def music_data(self):
        print(f'Name:{self.__genre},Salary:{self.__musician}')
m1=Music("Pop","Selena Gomez")
m2=Music("RnB","SZA")
m1.music_data()
m2.music_data()
