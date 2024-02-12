#packing items into a tuple
tuple1=(1, 'hello', 3.14, 'Mary',True)
print(tuple1)

#unpacking items and assigning them to variables
*a,b,c= tuple1
print("item assigned to 'a':", a)
print("item assigned to 'b':", b)
print("item assigned to 'c':", c)

#tuple comparison
tuple2=(1,2,3)
tuple3=(1,2,4)
print(tuple3 < tuple2) #outputs a False

#deleting a tuple
tuple4=(1,2,4,5)
# del tuple4
print(tuple4)

tuple5 =('John',False, 20, 0.7, 9)
slice_tuple = tuple5[1:2:3]
print(slice_tuple)
