def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")


def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
            print("Data written to the file successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def append_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data)
            print("Data appended to the file successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    filename = 'data.txt'

    print("1. Read from file")
    print("2. Write to file")
    print("3. Append to file")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        read_file(filename)
    elif choice == '2':
        data = input("Enter data to write to the file: ")
        write_to_file(filename, data)
    elif choice == '3':
        data = input("Enter data to append to the file: ")
        append_to_file(filename, data)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
