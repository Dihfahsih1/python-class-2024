list1=["John", False, 20, 0.7, 9]
print(len(list1)) #determine the lengh of the list

list1.remove(9) #removing a value from a list
print(list1)

print(3 in list1) 

#checking membership, for membership us "in"

#concatenating lists
list2= ["John", 20, 30 ]
new_list = list1 + list2 
print(new_list)

#clearing a list, Clear()removes everything from a list
list2.clear()
print(list2)

#count
count_items=new_list.count(20)
print(count_items)

#sort, for numbers only
unsorted_items=[29,3,0,1,5,80]
unsorted_items.sort()
print("These are the sorted items: ", unsorted_items)

#reverse items
unsorted_items.reverse()
print(unsorted_items)

#copyng
copied_list= unsorted_items.copy()
print(copied_list)