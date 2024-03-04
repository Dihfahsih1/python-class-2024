from queue import Queue

student_1 = input("Please enter student 1: ") 
student_2 = input("Please enter student 2: ") 
student_3 = input("Please enter student 3: ") 

student_queue = Queue()
student_queue.put(student_1)
student_queue.put(student_2)
student_queue.put(student_3)

new_student_queue = student_queue.get()
print("--------- output ---------------")

print(new_student_queue)