import timeit

# example 1
taken_time = timeit.timeit("print('Hello, World')", number=1)
print("Time Taken: ", taken_time, "seconds")

# example 2
# measuring time taken to run code
def square(n):
    return n**2

taken_time = timeit.timeit(lambda: square(5), number=100000)

print("Time Taken: ", taken_time, "seconds")

# example 3
taken_time = timeit.timeit("[x**2 for x in range(1000)]", number=100000)
print("Time Taken: ", taken_time, "seconds")