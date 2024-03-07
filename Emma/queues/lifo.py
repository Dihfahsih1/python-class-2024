#tack = []

#stack.append('action 1')
#stack.append('action 2')

#last_action=stack.pop()
#print(last_action)


def lifo():
    list = []
    input1 = input("Enter your first value : ")
    input2 = input("Enter your 2nd value : ")
    input3 = input("Enter youor 3rd value : ")

    list.append(input1)
    list.append(input2)
    list.append(input3)

    last_value = list.pop()
    print("Your value : ",last_value)


lifo()
