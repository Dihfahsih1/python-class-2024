#parameters are passed in the function call
def add(a=5,b=10):
    c=a+b
    print(c)

#arguments are passed in the function call
add(50)

def func1():
    average =(8/4)
    return average

def func3():
    print(func1())

def func2():
    print(func1())