import time
from sleeping_function import Task
def measure_time():
    task=Task()
    return task

start_time=time.time()
measure_time()
end_time=time.time()

elpsed time = end_time - start_time
print("Elapsed Time: ", elpsed_time, "seconds")


