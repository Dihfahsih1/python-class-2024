# square roots every number in the list comprehension
squared_list = lambda list_lambda: [x**2 for x in list_lambda ]
print(squared_list([1,2,3,4,5]))


# example 2
generate = lambda n: [x**2 for x in range(1, n+1)]
n = 5

squares = generate(n)
print(squares)