def function1():
    return "Hello"

def function2():
    x=function1()
    print(x, "world")
function2()


def add(a=5, b=10):     # arguments 5 and 10 are default values. if actual values are not given, a default answer is given
    c=a+b
    print(c)

add()

def add(a=5, b=10):
    c=a+b
    print(c)

add(10,10)

def add(a=5, b=10):          # the second value for b is taken from the placeholder
    c=a+b
    print(c)

add(1)

#how to call a function inside a function

def func1():
    average=(7/3)
    return average

def func2():
    print(func1())
    
func2()

def Name():
    name1= input("Enter your name:")
    return name1

def Age():
    age1=input("Enter your age:")
    print(Name(), age1)

Age()


#pass key word
def function():
    pass


def function():
    print("Not an empty function")