
#__main__ is a value that represents the top level environment where we run our code
def main():
    print(__name__, "This script run directly ")
   
if __name__ == "__main__": # it is so important to prevent automatic execution of our code in other modules
    main()
else:
    print('run from the import')


