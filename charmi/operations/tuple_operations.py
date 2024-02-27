#packing items into a tuple
tuple1=(1, 'hello', 3.14, 'Mary', True)
print(tuple1)

#unpacking items and assigning them to variables
a,*b,c = tuple1   #the * on b will assign a first then to c and the rest will be assigned to b
print("item assigned to 'a':", a)
print("item assigned to 'b':", b)
print("item assigned to 'c':", c)

#tuple comparison
tuple2=(1,2,3)
tuple3=(1,2,4)
print(tuple3 == tuple2) #outputs a False
print(tuple3 < tuple2)  #outputs a False because there are equal number of indices hence none of them is greater than the other

#deleting a tuple
# tuple4=(1,2,4,5)
# # del tuple4   #This will bring an error while printing tuple4 since itwas deleted
# print(tuple4)

#slicing a tuple
tuple5 = ('John', False, 20, 0.7)
slicing_tuple= tuple5[1:3] #This will only return from index1 and index2 because index3 is not inclued
slicing_tuple2= tuple5[1:2:3] #This will be looked at again 
print(slicing_tuple)