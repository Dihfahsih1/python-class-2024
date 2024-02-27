import os
def append_read_file():
    file_path ='files/data.txt'
    
    if os.path.exists(file_path):
        content_to_append=input("Enter content to append: ")
        with open(file_path, 'a+') as file:
            file.write(content_to_append + '\n')
            
            file.seek(0)
            
            file_content=file.read()
            
        return file_content
file_contents=append_read_file()
print(file_contents)   

        
        