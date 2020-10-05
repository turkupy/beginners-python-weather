# Weather Assembler
This app uses [OpenWeatherMap](https://openweathermap.org/) to fetch weather data.
```
Current     'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_token}'
Forecast    'http://api.openweathermap.org/data/2.5/forecast?q={city}&cnt={days_count}&appid={api_token}'
```

## Techniques you will need
* Define and call a [function](https://www.w3schools.com/python/python_functions.asp)
* Format strings using [f-strings](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python)
* Use [urllib](https://docs.python.org/3/howto/urllib2.html) to make requests to the API
* Create a [virtualenv](https://docs.python.org/3/library/venv.html) for managing dependencies

## Study project
0. Go to open weather map, create a user and API token. Explore the different APIs.
1. Copy the contents of `.env.dev` file into a new file named `.env`, create and fill in the missing API token.
1a. **If you are a beginner**, it is suggested that you go through the tutorial in `get_started.py` before continuing with the rest of the steps.
2. Create a python 3 virtualenv and install reqirements from `requirements.txt`.
3. Current weather:
* Prompt the user for a city name and fetch the current weather data using the current weather URL.
* Print city, country, temperature in celsius, humidity, weather type of the current weather data of the city.
* Make a function that converts temperatures from kelvin to celsius
4. Weather forecast:
* Prompt the user for a city name and a count of days and fetch the weather forecast using the forecast URL.
