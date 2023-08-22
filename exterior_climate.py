import json
import requests


class OpenWeather():
    def __init__(self, config_path: str):
        self.config = self.open_config(config_path)
        self.url = self.make_url(config_path)

    def open_config(self, config_path: str) -> dict:
        try:
            with open(config_path) as config_file:
                config = json.load(config_file)
        except json.JSONDecodeError as error:
            print(f"Error getting json file: {error}")
        except FileNotFoundError:
            print(f"Config file not found at {config_path}")
        return config
    
    def make_url(self, config_path):
        openweather_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = self.config["exterior_climate"]["openweather_apikey"]
        city = self.config["exterior_climate"]["city"]
        url = f"{openweather_url}appid={api_key}&q={city}"
        return url

    def get_weather(self):
        try:
            response = requests.get(self.url).json()
            data = {
                "temperature": round(Conversion.kelvin_to_celsius
                                    (response["main"]["temp"]), 2),
                "humidity": response["main"]["humidity"]
                # "weather_main": response["weather"][0]["main"]
            }
        except requests.HTTPError as error:
            print(f"Http error {error}")
        return data


class Conversion():
    def kelvin_to_celsius(kelvin):
        celsius = kelvin - 273.15
        return celsius
