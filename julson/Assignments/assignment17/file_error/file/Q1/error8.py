#InterruptedError: This error occurs when a system call is interrupted.

try:
    with open('file.txt', 'r') as file:
        content = file.read()
except InterruptedError:
    print("System call was interrupted.")