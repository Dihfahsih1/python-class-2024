import numpy as np

#addition of arrays
arr1= np.array([1,2,3])
arr2= np.array([4,5,6])

addition_result = arr1 + arr2
print(f"The sum of {arr1} and {arr2} is {addition_result}")

#subraction of arrays
arry1= np.array([4,5,6])
arry2= np.array([1,2,3])


subraction_result = arry1 - arry2
print(f"The difference of {arry1} and {arry2} is {subraction_result}")

#slicing and indexing arrays

array1 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

#print(array1[0,:])     #for accessing the first row
print(array1[:,0])      #for accessing first coloumn
print(array1[:2,:2])    #for accessing the first two rows and first two coloumns

#statistical operations on arrays

my_array= np.array([[1,2,3,4,5],
                    [6,7,8,9,1],
                    [2,3,4,5,6],
                    [7,8,9,1,2],
                    [3,4,5,6,7]])

mean_coloumn= np.mean(my_array, axis=0)
mean_row= np.mean(my_array, axis=1)

print("The sum of all coloumns is ", mean_coloumn)
print("The sum of all rows is ", mean_row)


#summing up all the array elements

