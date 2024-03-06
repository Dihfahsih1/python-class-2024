def create_file(filename):
    with open(filename, 'w') as file:
        print(f"File '{filename}' created successfully.")


def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of '{filename}':\n{content}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    
    def append_to_file(filename, content):
        with open(filename, 'a') as file:
            file.write(content)
            print(f"Content appended to '{filename}' successfully.")


    def main():
        while True:
            print("\nOptions:")
            print("1. Create a file")
            print("2. Read from a file")
            print("3. Append to a file")
            print("4. Exit")
            choice = input("Enter your choice: ")


            if choice == '1':
                filename = input("Enter filename: ")
                create_file(filename)
            elif choice == '2':
                filename = input("Enter filename: ")
                read_from_file(filename)
            elif choice == '3':
                filename = input("Enter filename: ")
                content = input("Enter content to append: ")
                append_to_file(filename, content)
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    