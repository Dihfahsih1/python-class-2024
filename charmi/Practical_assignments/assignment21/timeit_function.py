#The timeit() function executes time for small codes

import timeit
import time

# timeit.timeit(stmt= "", setup='', timer= time.perf_counter, number =)

#stmt is a statement passes. it can  be passed as a string or as a function.
#setup is the one that runs the code
#timer helps specify the timer to be used
#number specifies the number of times you want to function to run. the default is 1million

#example 1

execution_time = timeit.timeit("print('My name is Charmi')", number=1)
print("The time for execution is: ", execution_time)

#example 2

def addition(a,b):
    
    add = a+b
    return add



execution_time = timeit.timeit(stmt= "addition(1,2)", setup="from timeit_function import addition", number= 1)

print(f"The time for execution is {execution_time} seconds")

