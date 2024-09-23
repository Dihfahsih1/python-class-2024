import requests
# URL of the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"
#Making a GET request to a server
response = requests.get(url)
#checking if the request was successful
if response.status_code == 200:
    #parse the json response
    data = response.json()    
    #printing the first post
    print(data[1])    
else:
    print("Failed to retrieve data")