import timeit

# Define a function to time
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Create a Timer object with the function call to time
timer = timeit.Timer('fibonacci(10)', global=globals())


# Run the Timer and get the execution time
execution_time = timer.timeit()

print("Execution time", execution_time)