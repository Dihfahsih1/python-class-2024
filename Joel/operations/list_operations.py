list1 =['John',False, 20, 0.7, 9]
print(len(list1)) #determine the length of a list

list1.remove(9) #tremoving a value from a list
print(len(list1))

# for membership use in
print(False in list1)


# Concatenating lists
list2= ['John',20,30]
new_list = list1 + list2
print(new_list)

#clear() removes everything from a list
list2.clear()
print(list2)

#count
count_items=new_list.count('20')
print(count_items)

#sort(only sort numbers)
unsorted_items=[29,3,0,1,5,80]
unsorted_items.sort()
print("These are the sorted items:", unsorted_items)

#reverse items
unsorted_items.reverse()
print(unsorted_items)

#Copying
copied_list = unsorted_items.copy()
print(copied_list)