# __name__ this is a special built in variable in python that represents 
# the name of the current module when a python script is executed

# Why do we use if __name__ == "__main__"
# 1. It allows us to separate the code that should be run only when the script is executed  directly
# 2. It also checks if the script is imported as a module in another module.

#__name__ is a special python variable we use when interacting with modules
#-- It allows us to make a distinction between modules we import and those we don't

#__main__ is a value that represents the top level environment where we run our code
def main():
    print(__name__, "This script run directly ")
   
if __name__ == "__main__": # it is so important to prevent automatic execution of our code in other modules
    main()
else:
    print('run from the import')


