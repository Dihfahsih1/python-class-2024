class ImmutableTuple:
    def __init__(self,data):
        self.data=tuple(data)
        print(self.data)
num=ImmutableTuple([1,2,3])
# we are changing a list to a tuple is what ive done above
class Mutablelist:
    def __init__(self,data):
        self.data=data
lst=Mutablelist([1,2,3])


# exercise
class Immutablebool:
    def __init__(self,data):
        self.data=str(data)
        print(self.data)
bool=Immutablebool(False)
# exercise2
class Immutablestring():
    def __init__(self,data):
        self.data=int(data)
        print(self.data)
str=Immutablestring('Boy')
