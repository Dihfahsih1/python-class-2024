#max(), returns the largest item in an iterable or argument..
x = int(input("enter the first value: "))
y = int(input("enter the second value: "))
z = int(input("enter the third value: "))

Maximum = lambda x,y,z : max(x,y,z)
result = Maximum(x,y,z)
print (result)

print("The following will present minimum.")

a = int(input("enter the first value: "))
b = int(input("enter the second value: "))
c = int(input("enter the third value: "))

Minimum= lambda a,b,c: min(a,b,c)
result2= Minimum(a,b,c)
print (result2)