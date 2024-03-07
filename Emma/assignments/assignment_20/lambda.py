

list1 = [1,2,3,5,6,7,8,9]

is_min = lambda x: x==list1[0]
is_max = lambda x: x==list1[-1]
print("do you want to check for \n1. max\n2. min")
Input1 = input("Enter your answer : ")

if Input1 == "1" :
    Input2 = int(input("put in number to check : "))
    print(is_max(Input2))
    
 
elif Input1 == "2" :
    Input2 = int(input("put in number dto check : "))
    print(is_min(Input2))
else:
    print("no such option")

