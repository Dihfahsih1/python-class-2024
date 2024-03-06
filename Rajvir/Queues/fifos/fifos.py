from queue import Queue 

student_list =Queue()
student_list.put ("student1")
student_list.put("student2")
student_list.put("student3")

lining_students = student_list.get()

print(lining_students)