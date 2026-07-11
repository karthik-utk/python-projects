# Weather App (Python)

It is a simple weather app which shows the current weather and a 3-day forecast for a city. This is pure backend logic which demonstrates the use of an API in a simple way.

## Features

1. It uses a simple Python library, `requests`, to get a response from the API
2. It extracts temperature and description from a JSON API response
3. It allows user input for a city name of their choice
4. It handles the "city not found" error gracefully
5. It shows feels-like temperature and humidity too
6. It lets the user check multiple cities in a loop
7. It shows a 3-day forecast using the forecast endpoint

## How to Run

Requires Python 3 and the `requests` library:

```
pip install requests
```

Before running, set up your API key:
1. Copy `config_template.py` to a new file called `config.py`
2. Replace `REPLACE_WITH_YOUR_API_KEY` with your own OpenWeatherMap API key (get one free at openweathermap.org)

Then run:

```
python weather-app.py
```

## How It Works

- It uses two different API calls to get the current weather and the 5-day forecast, from which it only takes the details of 3 days by comparing the time to `12:00:00` and gives a 3-day forecast.
- It first loops through the API response and checks the `dt_txt` field, which contains a date and time. Since we only keep entries where the time is `12:00:00`, we get one value per day. From that data we extract useful info like temperature and humidity.
- The real API key is stored in `config.py` on the local laptop, and it is not pushed to GitHub because of `.gitignore`. If you want to use it, follow `config_template.py` and replace the placeholder with your own OpenWeatherMap API key.
- It handles invalid cities by giving a proper response instead of crashing.

## Example Usage

```
Enter a city name: London
Today's forecast: 

Temperature : 29.57
Feel like: 29.31
Humidity: 41
Description: clear sky
Next Three day forecast:

Day 1 weather report:

Temparture: 28.89
Feel like: 28.17
Humidity: 36
Description: clear sky

Day 2 weather report:

Temparture: 27.51
Feel like: 26.79
Humidity: 31
Description: broken clouds

Day 3 weather report:

Temparture: 31.45
Feel like: 29.93
Humidity: 27
Description: clear sky

Do you want to continue (y/n):
```

## What I'd Improve Next

- Try to improve the caching problems
- Optimize API calls
- Add a better GUI
- Get more forecast data