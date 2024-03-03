from queue import Queue

def student_line():

    student_queue = Queue()

    student1 = input("Enter name of student1: ")
    student2 = input("Enter name of student2: ")
    student3 = input("Enter name of student3: ")

    student_queue.put(student1)
    student_queue.put(student2)
    student_queue.put(student3)

    next_student = student_queue.get()
    print(next_student)

student_line()