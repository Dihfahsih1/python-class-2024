import json

with open("1MB.json", "r") as file:
    json_reader = json.load(file)
    print(json_reader)