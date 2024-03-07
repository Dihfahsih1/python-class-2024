from datetime import datetime

def time():
    current_time = datetime.now().strftime('%H:%M:%S')
    print('Current time:', current_time)

time()
