import requests

api_key='5ecbc1c45b756f07aa95e6bac961f916'

user_input=input("Enter city: ")

weather_data=requests.get(
    f'https//api.weathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}')
weather=weather_data.json()['weather'][0]['main']
temp=(weather_data.json()['main']['temp'])
print(weather,temp)