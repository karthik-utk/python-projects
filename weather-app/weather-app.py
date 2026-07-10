import requests
from config import api_key


a = 'y'

while a == 'y':
    city = input('Enter a city name: ')

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}')

    data = response.json()

    if data['cod'] == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        hum = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]

        print(f'Temperature : {temp} and humidity : {hum}')
        print(f'Description : {desc} and feels like: {feels_like}')
    else:
        print('City not found. Please check the spelling and try again.')

    a = input('Do you wan to continue (y/n): ')

