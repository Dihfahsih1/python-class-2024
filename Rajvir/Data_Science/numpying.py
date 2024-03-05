import numpy as np 

#subtructtion.
arr1 =np.array([1,2,3,4])
arr2 =np.array([5,6,7,8])

result = arr1 - arr2
# print(f'the answer of {arr1} and {arr2} is {result}')

#slicing and indexing of arrays.
my_array = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

# print(my_array[0,:]) row

#print(my_array[:,0]) column

#print(my_array[:2,:2])

#statistical operations on arrays.
my_array1 =np.array([[1,2,3,4,5],
                    [6,7,8,9,10],
                    [11,12,13,14,15],
                    [16,17,18,19,20],
                    [21,22,23,24,25]])
arr_row = np.mean(my_array1, axis=0)
arr_clm = np.mean(my_array1, axis=1)
print(arr_row)
print(arr_clm)
