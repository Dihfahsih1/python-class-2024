
def write_to_file(file_name, content):
    with open(file_name, "w") as file:
        file.write(content)
    print("Content written to ", file_name)


def read_from_file(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        
    print("Content read from ", file_name)
    print(content)



def append_to_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(content)
    print("Content appended to ", file_name)
    
    
def main():
    file_name = input("Enter a file name with extension (.): ")
    
    print("\n")
    print("------SELECT ONE OPTION PLEASE--------")
    print("\n")
    print("A. Write to file.")
    print("B. Read from file.")
    print("C. Append to a file.")
    print("\n")
    choice = input("Please enter your choice: ")
    
    if choice == "A" or choice == "a":
        content = input("Enter content to write to the file: ")
        write_to_file(file_name, content)
    elif choice == "B" or choice == "b":
        read_from_file(file_name)
    elif choice == "C" or choice == "c":
        content = input("Enter content to append to the file: ")
        append_to_file(file_name, content)
    else:
        print("Invalid choice")
        



# Data science in python involves the use of varius tools, libraries
# and techniques to analyze, visualize, and interpret large volumes of data



if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    