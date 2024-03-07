# numpy : large dimensional arrays(numerical computations)
import numpy as np

my_list = [1,2,3,4,5,6]
my_array = np.array(my_list)
#print(my_array)


   #array operations
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
# addition
result = arr1 + arr2
print(f"The sum of {arr1} and {arr2} is : {result}")
result2 = arr2 + arr1

print(f"the difference btn {arr2} and {arr1} is : {result2}")

  #trigonometric functions
result = np.sin(arr1)

   #slicing and indexing of arrays
my_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(my_array[0,0]) or
#print(my_array[0,:]) or
  # printing two rows at once
#print(my_array[:2,:2])

 #statistical operations on the way
my_array = np.array([[3,2,1,2,3],[3,4,6,4,6],[6,4,8,5,8],[5,6,7,4,6],[5,9,6,4,2]])
mean_r = np.mean(my_array,axis=1) # 0 axis showing all rows
mean_c = np.mean(my_array,axis=0) # 1 axis showing all columns
print(f"The mean of the rows, : {mean_r}")
print(f"The mean of the columns : {mean_c}")




