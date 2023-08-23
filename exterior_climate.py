import requests
import utilities
from datetime import datetime


class OpenWeather():
    def __init__(self):
        self.config = utilities.HelperFunctions.open_config("config.json")
        self.url = self.make_url()
        self.table_name = "exterior_climate"

    def make_url(self):
        openweather_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = self.config["exterior_climate"]["openweather_apikey"]
        city = self.config["exterior_climate"]["city"]
        url = f"{openweather_url}appid={api_key}&q={city}"
        return url

    def get_weather(self) -> dict:
        try:
            response = requests.get(self.url).json()
            data = {
                "datetime": datetime.now(), 
                "temperature": round(utilities.HelperFunctions.kelvin_to_celsius
                                    (response["main"]["temp"]), 2),
                "humidity": response["main"]["humidity"]
            }
        except requests.HTTPError as error:
            print(f"Http error {error}")
        return data

