def file():

    text= input("Enter the text of your choice to enter in the file: " + "\n")
  
    with open("text.txt", "w") as file:
        file.write(text)
    print("\n")

    print("\nWhat action do you want to perform on the data: ")
    print("A. Read")
    print("B. Append")

    choice = input("\nEnter your choice: ")

    if choice == "a" or choice == "A":
        print("\nYour text is as follows: ")
        file= open("text.txt","r")
        content = file.read()
        print(content)

    elif choice == "b" or choice == "B":
        text_append = input("\nEnter the text you want to append to the file: ")
        with open("text.txt", "a") as file:
            file.write(text_append)

        print("Your text has been appended!")

    else:
        print(f"Invalid choice: {choice}")

file()