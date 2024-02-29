def file_handling(filenmame):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content

    except FileNotFoundError:
        print("File not found")
        return None
# writing to a file
def write_to_file(filename, data):
    try:
        with open(filename,'w')as file:
            file.write(data)
            print("You have successful written to a file ")


    except Exception as e:
        print(f"An error occurred: {e}")


def find_and_replace(content, find_str, replace_str):
    replacement_content=content.replace(find_str, replace_str)
    return replacement_content

def string_to_upper(content):
    return content.upper()

def strip_content(content):
    return content.strip(" ")

def reverse_content(content):
    return content[:: -1]


if_name_=="_main_":
    filename="files/content.txt"
    data=input("Enter the data to be written")
    write_to_file(filename, data)

    #find content from the file

    file content=read_content(filename)
    if file_content:
        print("Original Content")
        print(file_content)


        file_content.find_and_replace(file_content, 'Python', 'Php')
        file_content.string_to_uppercase(file_content)
        file_content.stript_content(file_content)
        file_content.reverse_content(file_content)
        data=input("Enter the content: ")
        write to file(data, file_content)