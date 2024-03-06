import time

print("Hello")
time.sleep(1)
print("world")


for i in range(5):
    print('Task',i+1)
    time.sleep(1) #Delay of 5 seconds

#count down timer
seconds =3
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)
print('Pens down, time up')

def Task():
    print("Task Complete")
    
if __name__ == '__main__':
    time.sleep(3)
    Task()