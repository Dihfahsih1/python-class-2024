#timeit is a Python module and a function that is used to measure the execution time of small code snippets.

import timeit

code_snippet = """
result = [x for x in range(1000)]
"""

execution_time = timeit.timeit(stmt=code_snippet, number=1000)
print("Execution time:", execution_time)