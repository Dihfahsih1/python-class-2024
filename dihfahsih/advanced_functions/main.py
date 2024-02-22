# __name__ this is a special built in variable in python that represents 
# the name of the current module when a python script is executed

# Why do we use if __name__ == "__main__"
# 1. It allows us to separate the code that should be run only when the script is executed  directly
# 2. It also checks if the script is imported as a module in another module.
def first():
    print("first code")
def main():
    print("This script is being executed directly")
   
if __name__ == "__main__":
    main() 
    first() 


