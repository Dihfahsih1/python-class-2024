#using map function to create a lst from dictionary

def list_from_dict():

    student_dict = {"Charmi": "19", "Rajvir": "18", "Sarah": "43", "Mary": "90"}

    student_name_list = list(map(lambda x: x[0], student_dict.items()))
    student_age_list = list(map(lambda y: y[1], student_dict.items()))

    print(student_name_list)
    print(student_age_list)

list_from_dict()