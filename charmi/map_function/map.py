numbers = [1,2,3,4,5]

square = map(lambda x: x**2, numbers)

print(list(square))

#performing addition of one

def add_one():

    return x+1

x= [1,2,3,4,5]
result = map(add_one, x)
print(list(result))

add_one()

# squaring a range of numbers
def square():
    numbrs= range(1,8)
    squaring = map(lambda x: x**2, numbrs)

    print(list(squaring))
square()


