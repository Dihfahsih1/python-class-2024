students = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 43},
    {"name": "Jessca", "age": 20}
]

student = list(map(lambda person: person["name"], students))
print(student)