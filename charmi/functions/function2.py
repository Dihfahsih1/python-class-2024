def namefunc():
    name= "Charmi"
    return name

def age():
    age= 20
    print("Name:"+ namefunc() + ("\n") + "Age:" + str(age))      # empty quotes add space between the name and the age
                                                                 # since age is an integer, age must be made a string to add
age()





def Name():
    name1= input("Enter your name:")
    return name1

def Age():
    age1=input("Enter your age:")
    print(Name(), age1)

Age()