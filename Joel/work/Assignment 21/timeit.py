import timeit

timer = timeit.Timer('result = 2 + 2')


execution_time = timer.timeit()


print("Execution time:", execution_time)