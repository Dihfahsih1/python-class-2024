import csv

#creating a csv file and writing to it
with open("student.csv", "w") as csv_file:
    student_data = ("Charmi", "female")

    writer = csv.writer(csv_file)
    
    writer.writerow(student_data)

#appending to a csv file
with open("student.csv", "a") as csv_file:
    student_data2 = ("Rajvir", "female")

    writer = csv.writer(csv_file)
    
    writer.writerow(student_data2)
