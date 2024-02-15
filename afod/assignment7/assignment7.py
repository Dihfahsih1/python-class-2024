#what is the difference between a parameter and an argument in a function
# A parameter is a variable declared in the function definition.
# It represents a value that the function expects to receive when it is called.
# Parameters are placeholders for data that will be passed to the function when it is invoked.

# An argument is a value that is passed to a function when it is called.
# It is the actual value that is supplied to a function's parameter when the function is invoked.
# Arguments are provided in the function call to satisfy the parameters defined in the function's signature.

#what is the use of the return function
# The return statement in Python is used to exit a function and return a value to the caller. 
# When a return statement is encountered in a function, the function immediately exits
def add(a, b):
    return a + b

result = add(3, 4)
print(result)

def greet(name):
    print(f"Hello, {name}!")

result = greet("Alice")
print(result)