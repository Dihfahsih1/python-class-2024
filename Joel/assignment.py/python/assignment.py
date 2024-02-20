from datetime import datetime

def time():
    my_time = datetime.now().strftime('%H:%M:%S')
    print("Current time: ", my_time)0

time()