import json 
import requests


class OpenWeather():
    def __init__(self, config_path: str):
        try:
            with open(config_path) as config_file:
                self.config = json.load(config_file)
        except:
            

        openweather_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = self.config["exterior_climate"]["openweather_apikey"]
        city = self.config["exterior_climate"]["city"]
        self.url = f"{openweather_url}appid={api_key}&q={city}"

    def get_weather(self):
        response = requests.get(self.url).json()
        data = {
            "temperature": round(Conversion.kelvin_to_celsius
                                 (response["main"]["temp"]), 2),
            "humidity": response["main"]["humidity"]
            # "weather_main": response["weather"][0]["main"]
        }
        return data


class Conversion():
    def kelvin_to_celsius(kelvin):
        celsius = kelvin - 273.15
        return celsius


exterior_weather = OpenWeather("config.json")
print(exterior_weather.get_weather())


# def get_weather(city):
#     temprature = round(kelvin_to_celsius(response["main"]["temp"]), 2)
#     humidity = response["main"]["humidity"]
#     weather_main = response["weather"][0]["main"]
#     return temprature, humidity, weather_main