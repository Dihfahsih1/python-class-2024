from queue import queue

def student_line():

    student_queue = Queue()

    studt1 = input("Enter name of student1: ")
    studt2 = input("Enter name of student2: ")
    studt3 = input("Enter name of student3: ")

    student_queue.append(studt1)
    student_queue.append(studt2)
    student_queue.append(studt3)

    last_student = student_queue.pop()

    print(last_student)

student_line()