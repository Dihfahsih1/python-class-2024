

def LIFO():
    people_list = []
    
    person_1 = input("Please enter a person`s name: ")
    person_2 = input("Please enter a person`s name: ")
    person_3 = input("Please enter a person`s name: ")
    
    people_list.append(person_1)
    people_list.append(person_2)
    people_list.append(person_3)
    
    call_action = people_list.pop()
    print("------ output ------------")
    print(call_action)
    

if __name__ == "__main__":
    LIFO()
    