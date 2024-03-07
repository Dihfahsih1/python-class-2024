
 # use lambda with range of values
num= range(1,6)

func1 = map(lambda x : x**2 , num)
#print(list(func1))


 # use lambda with list comprehension

fruits = ["banana", "oranges", "dates"]
func2 = lambda x : x[:: -1]

list = [fruit for fruit in func2(fruits)] 
print(list)

