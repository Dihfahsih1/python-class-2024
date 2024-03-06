result = list(map(lambda x: x*2, range(3, 8)))
print(result)



#question2

nums = [1, 2, 3, 4, 5]
squared_nums = [lambda x: x**2 for x in nums]

# Calling the lambda function
result = [func(3) for func in squared_nums]
print(result)