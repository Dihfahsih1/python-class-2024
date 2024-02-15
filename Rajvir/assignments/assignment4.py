# How do we use comprehension in python

planets = [ "Mars", "Earth", "Jupiter", "pluto", "saturn"]
newlist= [planet for planet in planets if "a" in planet]

#for x in planets:
#if "a" in x:
#newlist.append (x) 
print (newlist)

#how to remove an element using pop 

k= [0, 1 , 44, 56, 72, 6]
popped_item= k.pop (3)
print (popped_item)
print(k)

#deleting in a dictionary 

countries= {"uganda": "kamapala", "kenya":"Nairobi"}
countries.pop("kenya")
print(countries)