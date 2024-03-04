

def enumarateApp():
    
    # student names
    student_name_1 = input("Please enter first student name: ")
    student_name_2 = input("Please enter second student name: ")
    student_name_3 = input("Please enter third student name: ")
    student_name_4 = input("Please enter fourth student name: ")
    print("\n")
    # student age 
    
    student_age_1 = int(input("Please enter first age name: "))
    student_age_2 = int(input("Please enter second age name: "))
    student_age_3 = int(input("Please enter third age name: "))
    student_age_4 = int(input("Please enter four age name: "))
    print("\n")
    # gender
    
    student_gender_1 = input("Please enter first student gender: ")
    student_gender_2 = input("Please enter second student gender: ")
    student_gender_3 = input("Please enter third student gender: ")
    student_gender_4 = input("Please enter fourth student gender: ")
    print("\n")
    # gender
    
    student_scores_1 = input("Please enter first student scores: ")
    student_scores_2 = input("Please enter second student scores: ")
    student_scores_3 = input("Please enter third student scores: ")
    student_scores_4 = input("Please enter fourth student scores: ")
    
    students_scores = {
        'name': student_name_1,
        'Age': student_age_1,
        'gender': student_gender_1,
        'scores': student_scores_1,
        
        'name': student_name_2,
        'Age': student_age_2,
        'gender': student_gender_2,
        'scores': student_scores_2,
        
        'name': student_name_3,
        'Age': student_age_3,
        'gender': student_gender_3,
        'scores': student_scores_3,
        
        'name': student_name_4,
        'Age': student_age_4,
        'gender': student_gender_4,
        'scores': student_scores_4,
        
    }
    
    for index,key in enumerate (students_scores):
        print(index, students_scores)
    
if __name__ == "__main__":
    enumarateApp()