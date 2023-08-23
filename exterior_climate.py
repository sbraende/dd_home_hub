import requests
import utilities


class OpenWeather():
    def __init__(self):
        self.config = utilities.HelperFunctions.open_config("config.json")
        self.url = self.make_url()

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
                "temperature": round(utilities.HelperFunctions.kelvin_to_celsius
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
