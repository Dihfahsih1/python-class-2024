import os

file_path ='files/data.txt'
if os.path.exists(file_path):
    
    with open(file_path,'r') as file:
        
        content=file.read()
        print(content)
else:
    print("file doesn't exist")