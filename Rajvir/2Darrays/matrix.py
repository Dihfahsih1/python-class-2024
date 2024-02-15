array1=[[1,2],
        [3,4],
        [4,5]]
print(array1[2][1])

#using loops
array1=[[1,2],
        [3,4],
        [4,5]]

for obj in array1:
    for element in obj:     #this is a loop in a loop 
        print(element, end="")
    print()

for obj in array1:
    for element in obj:     #this is a loop in a loop 
        print(element, end=",")    #this seperates elements with commas
    print()

for obj in range(5):  #this will print 4 objects 
    for ele in range(3):     #this will print 3 elements in each object
        print(f"[{obj} {ele}]")
    print()