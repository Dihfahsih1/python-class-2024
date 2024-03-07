from queue import Queue

def fifo():
    input1 = input("Put in first student's name : ")
    input2 = input("Put in second student's name : ")
    input3 = input("Put in third student's name : ")
    stud = Queue()
    stud.put(input1)
    stud.put(input2)
    stud.put(input3)

    student = stud.get()
   
    print(student)
    


fifo()



