ages = [5,10,6,40,20,30]

def myfunc(x):
    if x > 18:
        return False
    else:
        return True
    
adults = filter(myfunc,ages)

for x in adults:
    print(x)