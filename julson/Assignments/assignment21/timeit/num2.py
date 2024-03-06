#Measure the execution time of a dictionary comprehension

import timeit

code_snippet = """
result = {x: x**2 for x in range(1000)}
"""

execution_time = timeit.timeit(stmt=code_snippet, number=1000)
print("Execution time:", execution_time)