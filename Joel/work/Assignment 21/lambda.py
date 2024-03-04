# Lambda function for a range of values
range_lambda = lambda start, end, step: list(range(start, end, step))


# Using lambda with list comprehension
start = 1
end = 10 
step = 2
result = [x for x in range_lambda(start, end, step)]
print(result)