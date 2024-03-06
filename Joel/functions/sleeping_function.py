import time

print("Hello")
time.sleep(20)
print("world")


for i in range(5):
    print('Task',i+1)
    time.sleep(1) #Delay of 5 seconds

#count down timer
seconds =int input("Enter the starting time or seconds: "))
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)
print('Pens down, time up')