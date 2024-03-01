#using lambda function with a range of values

def list_comprehension():

    numbers = [1,2,3,4,5,6]

    even_number = []

    for number in numbers:
        even_number.append((lambda x: x%2==0)(number))

    for number in even_number:
        print(even_number)

list_comprehension()