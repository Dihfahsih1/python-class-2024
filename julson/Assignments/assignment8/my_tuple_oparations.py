#pack a tuble
tuple1=(1, "hello",3.14, 'Mary',True)
print(tuple1)

#unpacking items and assigning to varibles
a,*b,c = tuple1

print("Item assign to a :", a)
print("Item assign to b :", b)
print("Item assign to c :", c)

#tuple comparison
tuple2 = (1,2,3)
tuple3 = (1,2,4)
print(tuple1==tuple2)

#deleting a tuple
tuple4 = (1,2,3,4,5)
del tuple4
#print (tuple4)


tuple5 =("John",False,20,0.7,10,30)
slice_tuple = tuple5[1:5]
print("slice :",slice_tuple)