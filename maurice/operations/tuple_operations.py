# packing items
tuple1=(1, 'hello', 3.14,'hi','bye')
print(tuple1)

# unpacking items and assigning them to variables
a,*b,c=tuple1
print(a)
print(b)
print(c)

# tuple comparison
tuple2=(1,2,3)
tuple3=(1,2,4)
print (tuple2==tuple3) 

# deleting a tuple
tuple4=(1,2,3,4,5)
del tuple4

# slicing 
tuple5=('John',False,20,0.7)
slice_tuple=tuple5[1:3]
print(slice_tuple)
