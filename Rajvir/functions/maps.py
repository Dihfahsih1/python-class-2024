#squaring a list
number_list = [1,2,3,4,5,6,7]
squaring_list = map(lambda x : x**2, number_list)

print(list(squaring_list))

def add(x):
    return x+1
numbers = [1,2,3,4,5,6]
result= map(add,numbers)

print(list(result))

#range
numbers = range(1,8)

ranged_numbers =map(lambda x : x**2, numbers)
print(ranged_numbers)