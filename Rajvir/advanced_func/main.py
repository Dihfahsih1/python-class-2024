#__name__ is a special built variable in python that represents the name of the current module when a pythonscript is executed
#why do we use if __name__== "__main__"
# 1. it allows us to separate the code that should be run only when the script is executed.
#2. it also checks if the script is imported as a module in another module.
def first():
    print("first code")
def main():
    print("this script is being executed directly")

if __name__=="__main__":
    main()
    first()