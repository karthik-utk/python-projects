import requests
from config import api_key


a = 'y'

while a == 'y':
    city = input('Enter a city name: ')
    
    # Call 1: current weather
    current_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}')
    current_data = current_response.json()

    # Call 2: 3-day forecast
    response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}')
    data = response.json()

    if str(data['cod']) == '200' and str(current_data['cod']) == '200':
        i = 1

        print("\nToday's forecast: \n")
        print(f'Temperature : {current_data["main"]["temp"]}')
        print(f'Feel like: {current_data["main"]["feels_like"]}')
        print(f'Humidity: {current_data["main"]["humidity"]}')
        print(f'Description: {current_data["weather"][0]["description"]}')

        print('\nNext Three day forecast:\n')
        for entry in data['list']:
            if entry['dt_txt'].endswith("12:00:00") and i < 4:
                print(f'Day {i} weather report:')
                i += 1
                print(f'Temparture: {entry["main"]["temp"]}')
                print(f'Feel like: {entry["main"]["feels_like"]}')
                print(f'Humidity: {entry["main"]["humidity"]}')
                print(f'Description: {entry["weather"][0]["description"]}\n')
                
    else:
        print('City not found. Please check the spelling and try again.')

    a = input('Do you want to continue (y/n): ')

