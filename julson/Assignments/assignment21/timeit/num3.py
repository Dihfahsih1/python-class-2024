#Measure the execution time of sorting a list

import timeit

code_snippet = """
result = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
"""

execution_time = timeit.timeit(stmt=code_snippet, number=1000)
print("Execution time:", execution_time)