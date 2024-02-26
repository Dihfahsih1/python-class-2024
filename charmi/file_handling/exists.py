import os

def file_exists():

    file_path = "data.txt"

    if os.path.exists(file_path):
        new_data= input("Enter content to append: ")
        with open(file_path, "a+") as file:             #a+ is for appending and reading
            file.write(new_data + "\n")
            file.seek(0)      #seek is for moving the cursor from the start of the sentence to the end of the sentence
            content = file.read()

        return content
    
file_content = file_exists()
print(file_content)