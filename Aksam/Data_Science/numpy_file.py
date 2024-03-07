import numpy as np

my_array = np.array([[1,2,3],
                     [34,21,3],
                     [7,6,7]])
print(my_array[0,:]) # accessing first row

print(my_array[1,2])

mean_c = np.mean(my_array, axis = 0)
mean_r = np.mean(my_array, axis = 1)
print(f"The mean of the columns: {mean_c}")
print(f"The mean of the rows: {mean_r}")