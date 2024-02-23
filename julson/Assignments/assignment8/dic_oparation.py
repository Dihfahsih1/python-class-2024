dic1 = {'a':1, 'b':2}
dic2 = {'b':3, 'c':4}

#upsating a Dictionary
dic1.update(dic2)
print(dic1)

#comparison
dic3 = {'a':1, 'b':2}
dic4 = {'b':3, 'c':4}
print(dic3==dic4)

#length
print(len(dic1))

#sorting items in dict
dic5 = {'b':2, 'a':1,'c':3}
sorted_dic=dict(sorted(dic5.items()))
print(sorted_dic)