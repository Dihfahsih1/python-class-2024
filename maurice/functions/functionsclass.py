def name():
    name=input("Enter Your Name:  ")
    return name
def age():
    age=input("Enter Your Age:  ")
    # print("Name:  " + name() + ('\n') + "Age: " + str(age) )
    print(name(),age)

age()
        