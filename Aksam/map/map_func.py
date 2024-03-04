
# def addOne(num_1):
#     return num_1 + 1

# numbers = [1,2,3,4,5]
# result = map(addOne, numbers)

# print(list(result))

numbers =  range(1,8)
double_numbers = map(lambda x:x**2, numbers)
print(list(double_numbers))


