import requests
import simplejson # Remove later

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = open("api_key", "r").read()

city = "Fornebu"

url = base_url + "appid=" + api_key + "&q=" + city

# response = requests.get(url).json()
response = requests.get(url).json()

print(response)


# print(simplejson.dumps(response, indent = 4, sort_keys = True)) # remove later

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

#print(response("main"))

temp_kelvin = response["main"]["temp"]

print(kelvin_to_celsius(temp_kelvin))


