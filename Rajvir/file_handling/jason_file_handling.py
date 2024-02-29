import json

with open("files/json1.json", "r") as file:
    data = json.load(file)
    print(data)