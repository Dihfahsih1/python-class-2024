import time

#Counting down using while loop and delaying by 1 second
number = int(input("Enter the number to count down from:"))

while number > 0:
    print(number)
    time.sleep(1) 
    number -= 1 

print("Time up!")