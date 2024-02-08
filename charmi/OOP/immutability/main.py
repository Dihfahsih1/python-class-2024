# mutable classes

class MutableList:

    def __init__(self,values):
        self.values= values

lst=MutableList([1,2,3,4,5,6])

# immutable boolean class

class ImmutableBoolean:

    def __init__(self, data):
        self.data=data
        print(self.data)

boo= ImmutableBoolean(True)

# immutability string class

class ImmutableString:

    def __init__(self, values):
        self.values=values
        print(self.values)

strn= ImmutableString("Charmi Panchal")