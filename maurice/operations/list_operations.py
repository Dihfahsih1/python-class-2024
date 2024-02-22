list1=['John',False,20,0.7,9]
# removing an item .remove(item) 
list1.remove(9)
print(list1)
# to know the length of a list(no of items in the list)  len
print(len(list1))
# checking membership of an item in a list   in
print(20 in list1)
# concatinating lists(joining lists)   +
list2=['John',20,30]
new_list=list1+list2
print(new_list)
# clearing a list clear    .clear()
cleared_list=list2.clear()
print(cleared_list)
# count-tells you how many times an item appers in a list   .count(item)
count_items=new_list.count("John")
print(count_items)
# sort(we only sort numbers)   .sort() it only works for integers and floats (arranges them in ascending order)
unsorted_items=[29,3,0,1,5,80]
unsorted_items.sort()
print("These are the sorted items: ", unsorted_items)
# reverse
unsorted_items.reverse()
print(unsorted_items)
# copying
copied_list=unsorted_items.copy()
print(copied_list)

