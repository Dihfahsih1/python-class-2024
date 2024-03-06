import time

print("Processing........................")
time.sleep(2)
print("Processing complete")


for i in range(5):
    print("Task", i+1)
    time.sleep(1)
    

# count down timer

seconds = int(input("Please the starting time or seconds: "))
for sec in range(seconds, 0 ,-1):
    print(sec)
    time.sleep(3)
print("Time up")

# def task():
#     seconds = int(input("Please the starting time or seconds: "))
#     for i in range(seconds):
#         print("Task", i+1 )
#         time.sleep(3)
#         print("All tasks runned successfully with 0 errors") 
        
# task()

def Task():
        print("Task complete")
        


if __name__ == "__main__":
    time.sleep(3)
    Task()