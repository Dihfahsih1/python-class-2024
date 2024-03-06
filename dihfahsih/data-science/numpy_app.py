import csv
import numpy as np

class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def __str__(self):
        return f"Name: {self.name}, Age:{self.age}, Salary:{self.salary}"
    
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department=department
        
    def __str__(self):
        return f"Name: {self.name}, Age:{self.age}, Salary:{self.salary}, Department: {self.department}"
    
def read_employee_from_csv(file_path):
    employee=[]
    with open(file_path,'r') as file:
        reader=csv.reader(file)
        
        for row in reader:
            if len(row) == 3:
                name, age, salary=row
                employee.append(Employee(name,age,salary))
            elif len(row) == 4:
                name, age, salary, department=row
                employee.append(Manager(name,age,salary, department))
        return employee
    
def calculate_average_salary(employee):
    salaries=np.array([emp.salary for emp in employee])
    return np.mean(salaries)


def sort_employees_by_age(employee):
    return sorted(employee, key=lambda emp: emp.age)

if __name__=='__main__':
    file_path="employee.csv"
    employees= read_employee_from_csv(file_path)
    
    print('Employees:')
    for emp in employees:
        print(emp)
            
    avg_salary=calculate_average_salary(employees)
    print(f"\nAverage Salary: {avg_salary}")
    
    sorted_employees=sort_employees_by_age(employees)
    print("\n Employees sorted by age:")
    for emp in sorted_employees:
        print(emp)
    
    
    