# create a lambda function with a range of values
def fuc():
    squared_values = lambda start, end: [(x, x**2) for x in range(start, end)]

    # Usage
    start_value = 1
    end_value = 6
    result = squared_values(start_value, end_value)
    print(result)
fuc()

#use lambda eith list comprehension
start_value = 1
end_value = 6

squared_values = lambda start, end: [(x, x**2) for x in range(start, end)]

result = squared_values(start_value, end_value)
print(result)
# Inside the lambda function, we use list comprehension to generate a list of tuples containing each number in the range and its square.
# 
from abc import ABC, abstractmethod
import cmath

class SquareRootFinder(ABC):
    @abstractmethod
    def find_square_root(self, num):
        pass

class CustomSquareRootFinder(SquareRootFinder):
    def find_square_root(self, num):
        return cmath.sqrt(num)

# Create an instance of the subclass
finder = CustomSquareRootFinder()

# Call the method to find the square root of -9
result = finder.find_square_root(-9)
print("Square root of -9:", result)
# def process_info(person):
#     # Process the information here, for example, you can convert the age to integer
#     person['age'] = int(person['age']) * 2  # Just an example, you can modify as needed
#     return person

# # Dictionary with names and ages
# people = [
#     {'name': 'Alice', 'age': '30'},
#     {'name': 'Bob', 'age': '40'},
#     {'name': 'Charlie', 'age': '50'}
# ]

# # Map the process_info function to each person in the list of dictionaries
# processed_people = list(map(process_info, people))

# # Print the result
# print(processed_people)

def process_info(person):
    person['name'] = person['name'][::-1]
    return person

people = [
    {'name': 'Alice', 'age': '30'},
    {'name': 'Bob', 'age': '40'},
    {'name': 'Charlie', 'age': '50'}
]
processed_people = list(map(process_info,people))
print(processed_people)