#using a while loop to create a count down method..
import time 

print("The following will begin a countdown ending with time up.")


number = int(input("Enter the seconds to countdown from: "))
i = int(input('enter the value to end.: '))
while  number <= i:
    print(number)
    number += 1 

    time.sleep(1)
print("Time is up!")
