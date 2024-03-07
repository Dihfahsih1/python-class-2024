num = [1,2,3,4,5,6]

double_numbers = map(lambda x:x*2,num)

square_num = map(lambda x: x**2,num)
#print(list(square_num))

#mapping a function to convert strings to uppercase

words = ['Hello','world']
Upper_case = map(str.upper,words)


# map function that performs an addition

def add_one(x):
    return x+1

numb = [1,2,3,4,5]
result = map(add_one,numb)
#print(list(result))


 # create a map function for  range of numbers 1 - 8 and square them then print a list on the squared numbers

list1 = range(1,8)

numb_square = map(lambda x: x**2,list1)
print(list(numb_square))



