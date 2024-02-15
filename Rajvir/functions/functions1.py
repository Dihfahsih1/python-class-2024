def func1():
    return "hello"

def func2():
    x=func1()
    print (x, "worlds")
func2()
def greet():
    return "namaste"

def world():
    x=greet()
    print (x, "India")
world()
# testing
# casting 
def add(a=5, b=10):
    c= a+b
    print(c)
                                     # par> arg
add(50,60) 
# arguements are passed in the function call 
def func1():
    average=(7/3)
    return average

def func2():
    print (func1())
func2()

def function():
    pass 

def function2():
    print("not empty")
