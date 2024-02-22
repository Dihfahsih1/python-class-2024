# mutable classes list
class MutableList:
    def __init__(self, values):
        self.values = values
    
lst  = MutableList([1,2,3,4])

# mutable class dicts
class MutableDict:
    def __init__(self, values):
        self.values = values
    
dct  = MutableList({"a":1,"b":2})

class MutableData:
    def __init__(self, data):
        self.data = list(data)
    
mutable_data = MutableData([1,3,4])


# immutable int class
class ImmutableInt:
    def __init__(self, values):
        self.values = values
num = ImmutableInt(5)

# immutable tuples class
class ImmutableTuple:
    def __init__(self, values):
        self.values = tuple(values)
        print(self.values)
immut_tuple = ImmutableTuple((1,2,4,5))

# ========================== 
# CLASS ASSIGNMENT
# ==========================

# immutable boolean class
class ImutableBoolean:
    def __init__(self, data) -> None:
        self.data = bool(data)
        print(self.data)
immut_bool = ImutableBoolean(5 > 6)

# immutable string class
class ImmutableString:
    def __init__(self, data):
        self.data = str(data)
        print(f"{self.data}, world")

immut_str = ImmutableString("Hello")

