#list comprehension using lambda.
list1= [1,2,3,4,5,6,7,8]
compre_list =list((lambda x: x+1 )(x) for x in list1)
print(compre_list)