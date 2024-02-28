
list1 =["John",False,20,0.7,10,30]
print(len(list1)) #to determine length of a list
list3=[1,2,3,4,5]
list3.remove(1)
print("List 3 :",list3)
#list1.remove(2)  # to remove a value from a list
#print(list1)

print(False in list1) #in is use for membership

#Concartinating lists
list2 = ["John",20,30]
new_list = list1 + list2
print (new_list)

#clearing a list, removes everything from a list
#cleared_list = list2.clear

#Count
count_items = new_list.count('20')
print(count_items)

#sort only works for numbers
unsorted = [29,30,40,1]
#sorted_items = new_list.sort()
unsorted.sort()
print ("Thise are the sorted items: ",unsorted)

#reverse sort
unsorted.reverse()
print(unsorted)

#coping
copied = unsorted.copy()
print(copied)