import timeit


timer = timeit.Timer('[x for x in range(1000)]')


execution_time = timer.timeit()


print("Execution time:", execution_time)