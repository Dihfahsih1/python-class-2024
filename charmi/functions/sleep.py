import time

print("Hello")
time.sleep(1)
print("World")

for i in range(5):
    print('Number', i+1)
    time.sleep(1)

number = int(input("Enter the seconds to countdown from: "))
for i in range(number, 0, -1):
    print(i)
    time.sleep(1)
print("Time is up!")

def task():
    print('Task complete')
if __name__ == "__main__":
    time.sleep(3)
        
    task()