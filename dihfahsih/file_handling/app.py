def read_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None

def append_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data)
            file.seek(0)
            print("Successfully written to file:", filename)
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")

def find_and_replace(content, find_str, replace_str):
    return content.lower().replace(find_str.lower(), replace_str, -1)

def string_to_lower(content):
    return content.lower()

def strip_content(content):
    
    return content.strip(',')

def reverse_content(content):
    return content[::-1]

if __name__ == "__main__":
    # append to file
    new_data=input("Enter the data to append: ")
    
    filename = "files/content.txt"
    append_to_file(filename, new_data)
     
    # Find content from the file
    file_content = read_content(filename)
    if file_content:
        print("Original Content:")
        print(file_content)
        
        # Apply transformations
        file_content = find_and_replace(file_content, 'python', 'Php')
        file_content = string_to_lower(file_content)
        file_content = strip_content(file_content)
        file_content = reverse_content(file_content)
        
        
