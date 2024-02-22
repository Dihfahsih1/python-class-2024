#mutable class list
class MutableList:
    def __init__(self, values):
        self.values=values
        
lst=MutableList([1,2,3,4])

#mutable class dicts
class MutableDict:
    def __init__(self, values):
        self.values=values
        
dct=MutableDict({'a':4,'b':2})

class MutableData:
    def __init__(self, data):
        self.data=list(data)
        
mutable_data=MutableData([1,3,4])


#immutable int class

class ImmutableInt:
    def __init__(self, values):
        self.values=values
num=ImmutableInt(5)

#immutable tuples
class ImmutableTuple:
    def __init__(self, data):
        self.data=tuple(data)
        self.data=(1,3,4,5,6)
        self.data[0]=2
        print(self.data)
        
num=ImmutableTuple([1,2,3,4])

