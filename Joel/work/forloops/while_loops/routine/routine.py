def greet():
    return("Hello, welcome to our program")

def ask_name():
    name = input("What is your name? ")
    return name

def main():
    greet()
    name = ask_name()
    print("Nice to meet you, {}!".format(name))
    # Add more tasks here if needed

if __name__ == "__main__":
    main()