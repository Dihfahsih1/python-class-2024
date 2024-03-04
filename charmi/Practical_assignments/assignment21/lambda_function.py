#using lambda function with a range of values

def list_comprehension():

    numbers = [1,2,3,4,5,6]

    even_list = list((lambda x: x%2==0)(x) for x in numbers)  #thi print true if even and false if odd

    print(even_list)

list_comprehension()