import numpy as np


my_list =[1,2,4,5,6]
my_array=np.array(my_list)
print(my_array)

#array operations
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

#addition
result= arr1 + arr2
print(f'The sum of {arr1} and {arr2} is: {result}')

#trigonometric functions
result=np.sin(arr1)

#slicing and indexing of arrays
my_array=np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(my_array[0,:]) #accessing first row

print(my_array[:2,:2])

#statistical operations on the array(mean, median, sd, range, average)
mean_c = np.mean(my_array, axis=0)
mean_r =np.mean(my_array, axis=1)
print(f"The mean of the columns: {mean_c}")
print(f"The mean of the rows: {mean_r}")

#summing up all the elements
total_sum = np.sum(my_array)
print(f"The total sum is: {total_sum}")

