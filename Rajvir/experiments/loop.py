#printing 1 to 100 using loop

for num in range(1,101):
    print (num)

#printing odd numbers from 1 to 10

for num in range(1,10,2):
    print(num ,'\n') 

#while
a = int(input("any number you want: "))
while (a < 10):
    print(a, end=" " + "\n")
    a=a+1 #update the value by num by 1

count = 10
while(count>0):
    print(count, end=" ") 
    count = count -2