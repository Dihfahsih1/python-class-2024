
students = ["emmma", "joel","charmi", "affod", "rajvir","mumbere","aksam"]
index =0

#while index<len(students):
#print(students[index])
# index += 1

while index < len(students):
    student_name = students[index]
    attendence = input(f"Is {student_name} present? (yes/no): ").lower

    if attendence == "yes":
        print(f"{student_name} is present.")
    elif attendence == "no":
        print(f"{student_name} is absent.")

    else: 
        print("invalid input. please enter yes and no.")

    index += 1  

