import os
file_path='files/data.tx'
try:
    file=open(file_path,'r')
    print(file.read())
except FileNotFoundError:
    print("File Does not exist")
    
except PermissionError:
    print("You have no permission to access this file")

finally:
    if os.path.exists(file_path):
        file_path.close()
    else:
        print("File can't be closed cos it was never opened")
    
    