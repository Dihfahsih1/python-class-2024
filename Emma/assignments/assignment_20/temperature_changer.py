

print("what would you like to do ?")
print("1. degrees celicius to fahrenheit\n2. fahrenheit to degrees celicius")
Input1 = input("enter option : ")
def celicius():
    Input2 = int(input("enter your value in fahrenheit : "))
    answer = (Input2-int(32)/int(1.8))
    print("Your temperature in celcius : ",answer,"C")

def fahrenheit():
    Input2 = int(input("enter your value in celicius : "))
    answer= (1.8*Input2)+32
    print("Your temperature in fahrenheit : ",answer,"F")

if Input1 == "1":
    fahrenheit()
elif Input1 == "2":
    celicius()
    
