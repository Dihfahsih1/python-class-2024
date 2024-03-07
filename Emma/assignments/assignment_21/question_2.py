from math import sqrt
list1 =[
    {'name':'James','age': 20},
    {'name': 'Alex', 'age': 21}
    ]

function_lambda = map(lambda x : x[::-1], list1[0]['name'])
print(list(function_lambda))

print(sqrt(16))