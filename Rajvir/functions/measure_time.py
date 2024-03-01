import time
from sleep import task

def measuring_time():
    task = task()
    return task

start_time = time.time()
measuring_time()

end_time = time.time()

elapsed_time = end_time- start_time
print("Elapsed time: ", elapsed_time, " seconds")
