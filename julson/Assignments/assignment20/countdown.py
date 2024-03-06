import time

countdown = int(input("Enter Starting Number : "))

while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown -= 1

print("You Have been Hacked!")