# A step-by-step tutorial of an API call to OpenWeather
# Go through this example before completing the other challenges from the template
# Comment out some of the "prints" to be able to avoid a cluttered output
# To make a commented line, use the hashtag. Your Python program will ignore any line that starts with a hashtag

# we need to import modules (libraries with ready made code) to get some functions
# that already exist out there. thanks to other developers we don't need to waste time writing everything from scratch!

# for now just import the modules mentioned here. if you are really curious what they do,
# feel free to google "what does Python XYZ module do?"

import os
import json

# prints pretty JSON
from pprint import pprint

# urllib is a module used to fetch and handle URLs (e.g. open, read, parse URLs, etc.)
from urllib import request 
# dotenv should be installed (with pip) before importing it
from dotenv import load_dotenv

# this loads variables from the .env file, where you specified your token
# the .env file should be in the same folder as this get_started.py file
load_dotenv()

# os.getenv() returns the value assigned to OWM_TOKEN
api_token = os.getenv("OWM_TOKEN")

# Specify a city for the forecast information
# Quotation marks tell your Python program that your city variable is a string (e.g. characters)
city = 'Helsinki'

# API call to OpenWeather 
# Retrieves information for the specified CITY
# format() uses {} as placeholders for the variables (e.g. city & api_token) you specify in the parentheses
city_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_token)

# urlopen() opens a URL
# the response is an HTTP response
response = request.urlopen(city_url)
# let's read the response we get
data = response.read()
# read() returns bytes, but let's use decode() to convert from bytes to strings
# bytes are machine readable, strings are only human readable
data = data.decode()

# our reponse data is a JSON string
#print(data)

# now we need to convert it from a string to a JSON dictionary for easier access
data_dict = json.loads(data)

# pretty-print our json to make it more readable
#pprint(data_dict)

# now we want to parse our JSON dictionary (what's a dictionary? https://realpython.com/python-dicts/)
# in this particular example, "base", "clouds", "cod", etc. are KEYS, and "stations", "{'all': 20}", "200", etc. are corresponding VALUES
# dictionaries can be nested: values can be dictionaries (or lists) (what's a list? https://realpython.com/python-lists-tuples/)

# for example, the values for the keys "main" and "sys" are dictionaries (because they have curly brackets)
# and the value for the key "weather" is a list (because they have square brackets [])

# we can retrieve information from the values by indicating the key we want to get them from
weather_id = data_dict['id']
print(weather_id)

# let's get the temperature information
weather_temp = data_dict['main']
print(weather_temp)
# type() tells you the variable type: string, integer, list, etc.
# it's a dictionary
print(type(weather_temp))

# let's get max temp
max_temp = weather_temp['temp_max']
print('Maximum temperature is {}'.format(max_temp))

# let's get information from 'weather' key
weather = data_dict['weather']
#print(weather)

# Uncomment and see if this works
#description = weather['description']
#print(description)

# this can be tricky, but this is a list of dictionaries (or 1 dictionary, to be precise)
# len() can tell us how many items are in a dictionary (also in a list and string)
print(len(weather))

# lists start at 0: 0, 1, 2, 3, 4...
# to get the first and only item of this list, we need to indicate the first index, e.g. zero
weather_info = weather[0]
print(weather_info)

# weather_info is a dictionary. can you retrieve information from here using the previous examples? :)
# ...
# ADD your own code here!

# let's create a function
# a function is a block of code that is executed only when it's called
# first, let's create one. you need to use 'def' to let your program know it's a function
def my_function():
    a = 3
    b = 2
    my_sum = a + b
    print(a + b)

# at this point the function won't output anything because we have not called it yet
# let's call the function!
my_function()

# our my_function() uses the variable we defined inside the function (a, b) to calculate the sum
# but if i want to calculate many different sums? let's use arguments!

def function_with_args(a, b):
    my_sum = a + b
    print(my_sum)

# let's call the function! and let's not forget to define a and b before that!
a = 4
b = 7
function_with_args(a, b)

# now we can get a different sum using some other variables!
# the names of the variable do not need to be the same as the function arguments
# this works:
apples = 10
oranges = 2
print('Counting fruit')
function_with_args(apples, oranges)

# if you are up for another challenge, check out how to use user input from the link below:
# https://www.geeksforgeeks.org/taking-input-in-python/