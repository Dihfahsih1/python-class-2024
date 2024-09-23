# Finding out if a name starts or ends wiht a vowel

def vowels():

    students= ['Charmi', 'Rajvir', 'Joel', 'Emma', 'Aksam', 'Affod', 'Mumbere']
    index= 0

    while index < len(students):
        #Using if to get names whose names start with a vowel
        if students[index][0].lower() in ['a', 'e', 'i', 'o', 'u']:
            print(f"{students[index]} starts with a vowel.")

        else:
            print(f"{students[index]} does not start with a vowel.")
        index += 1

    print('*'*20)

    for student in students:   
        #Using if to get names that end with a vowel
        if student[-1].lower() in ['a', 'e', 'i', 'o', 'u']:  #While using 'for' we dont write [index][-1]
            print(f"{student} ends with a vowel.")            #While using 'for' we dont insert [index]

        else:
            print(f"{student} does not end with a vowel.")

vowels()
