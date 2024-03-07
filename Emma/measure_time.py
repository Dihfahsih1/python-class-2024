import time
from sleeping_func import task

start_time = time.time()
end_time = time.time()

elpsed_time = end_time - start_time

#print("Elapsed Time : ", elpsed_time, "seconds")

task()

