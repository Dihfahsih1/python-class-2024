import time


def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Countdown complete!")


countdown(10) # Replace 10 with the number of seconds you want to countdown from