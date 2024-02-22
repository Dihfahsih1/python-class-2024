# #__name__ is a special builtin variable in python
# #it represents the current module when python script is executed

# Why do we use if __name__ == "__main__"?
# 1. It allows us to separate the code that should run only when the script is executed
# 2. It also checks if the script is imported as a module in another module

def first():
    print("First code.")
def main():
    print("This script is being executed directly")

if __name__== "__main__":
    main()
    first()