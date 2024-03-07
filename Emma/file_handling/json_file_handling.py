import json

with open("files/sample.json",'r') as file:
    data=json.load(file)
    print(data)