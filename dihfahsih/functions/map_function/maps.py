#Double numbers in a list
numbers = range(1,8)

double_numbers=map(lambda x:x**2, numbers)

print(list(double_numbers))

#mapping a function to convert strings to uppercase

words=['Hello', 'World']
upper_case=map(str.upper, words)
print(list(upper_case))

def add_one(x):
    return x+1
numbers=[1,2,3,4,5]
result=map(add_one,numbers)

print(list(result))