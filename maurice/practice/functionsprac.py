# parameter are passed in function definition
def add(a,b):
# argument arepassedin the function call
    return a + b 
print(add(4,6))

def greet(name):
    print("hello",name)
name=['Van','Mary']
greet("Mary")
# return
def of(a,b):
    return a*b
result=of(6,8)
print(result)
# in class 
def add(a=5,b=10):
    c=a+b
    print(c)
add(50,60)

# tr
def func1():
    average=(8/2)
    return average
def func2():
    print(func1())
