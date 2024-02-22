
#mutable class list
class MutableList:
    def __init__(self,values):
        self.values = values


lst =MutableList([1,2,3,4,5])


#mutable class dicts
class MutableDict:
    def __init__(self,values):
        self.values = values


dct =MutableDict({'a':1,'b':2})

class MutableData:
    def __init__(self,data):
        self.data = list(data)

mutable_data=MutableData([1,3,4])


# immutable int class

class ImmutbaleInt:
    def __init__(self,values):
        self.values = values
num = ImmutbaleInt(5)

# immutable tuples
class ImmutableTuples:
    def __init__(self,data):
        self.data=tuple(data)

num=ImmutableTuples([1,2,3,4])


# immutable Boolean
class ImmutableBoolean:
    def __init__(self,data):
        self.data=bool(data)
        print(f"it is {self.data}")
num=ImmutableBoolean(3==1)

# immutable string
class ImmutableString:
    def __init__(self,data):
        self.data=str(data)
        print(f"This is a {self.data}")

num=ImmutableString("Fish")

        

G