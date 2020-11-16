import os
import json
import pprint

from urllib import request
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv("OWM_TOKEN")

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    # Let's remove floating points
    celsius = int(celsius)

    return celsius

def get_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_token)
    
    try:
        req = request.urlopen(url)
        data = req.read().decode()
        json_ = json.loads(data)


        temp = json_['main']['temp']
        feelslike = json_['main']['feels_like']
        sky = json_['weather'][0]['description']
        # Let's add uppercase letters
        sky = sky.title()

        temp = kelvin_to_celsius(temp)
        feelslike = kelvin_to_celsius(feelslike)

        return (temp, feelslike, sky)
    except:
        return None
