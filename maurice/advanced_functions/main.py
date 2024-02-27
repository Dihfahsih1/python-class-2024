# __name__ this is a special buit in variable in python that represents the name of the current module when a python script is executed

# why we use "if __name= "__main__""
# 1, It allows us sto separate the code that should be run only when the script is executed 
# 2.It also checks if the script is imported as a module in another module.


def calculation(a,b):
    a=input('enter no1: ')
    b=input('enter no.2: ')
    return a*b 
print(calculation(4,5))
def main():
    print('This script is being executed')
if __name__=="__main__":
    main()
    