import time
n = 10
for i in range(1,6,1):
    print(i+1)
    time.sleep(1)


seconds = int(input("Enter the starting time or second :"))
for i in range(seconds,0,-1):
    print(i)
    time.sleep(1)
# function called task , print task complete after 3 seconds
    
def task():
    time.sleep(3)
    print("task complete")

if __name__ == "__main__":
    task()