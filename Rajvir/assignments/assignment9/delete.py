#Example 1

class Myclass:
    name="john"

del Myclass

print(Myclass)  #it will show an error because it is no longer defined..

#example 2

x= "hello"
del x
print (x) #same here

#deleting from a list..
x = ["apple", "banana"]
del x[0]

print (x)

