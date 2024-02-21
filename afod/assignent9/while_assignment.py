students= ["emma", "joel", "charmi","afod","rajvil","mumbeere","maurice", "axsam"]
index =0

while index<len(students):
   print(students[index])
   index += 1

while index < len(students):
    student_name = students[index]
    attendance = input(f"Is {student_name} present? (yes/no): ").lower()
    
    if attendance == "yes":
        print(f"{student_name} is present.")
    elif attendance == "no":
        print(f"{student_name} is absent.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

    index += 1