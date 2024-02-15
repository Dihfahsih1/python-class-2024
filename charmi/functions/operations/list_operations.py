list1 = ['John', False, 20, 0.7, 9]
list1.remove(9) #this will remove 9 from the list. note:insert the exact value to remove not its index
print(list1)
print(len(list1)) # len is to determine length of a list


#Checking for membership
print(False in list1)  #this will check if False is in the list therefore it will return a True
print(3 in list1)   # this will return a True

#Concatenating lists
list2= ['John', 20]
new_list = list1 + list2  #concatenating will add the two lists
print(new_list)

#Clearing a list 
list2.clear()   #clearing removes everyting from a list
print(list2)

#Count
count_items= new_list.count('John')  # this will count how many times John enters
print(count_items)

count_items2 = new_list.count('20')  #This will return 0 because integars are not supposed to be in strings.
print(count_items2)

#Sort
unsorted_items= [29, 8, 6, 20, 100]
unsorted_items.sort()
print("These are sorted items:", unsorted_items)

#reverse items
unsorted_items.reverse()
print("These are reversed items:", unsorted_items)

#Copying
copied_list = unsorted_items.copy()
print(copied_list)