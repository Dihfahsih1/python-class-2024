num1 = 5
num2 = 2

result = list(filter(lambda x: x>0, [num1-num2]))[0] 

#if result:
    #print("num1 is greater than num2")
#else:
    #print("num1 is not greater than num2")
print(result)