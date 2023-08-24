import json


class HelperFunctions():
    def open_config(config_path: str) -> dict:
        try:
            with open(config_path) as config_file:
                config = json.load(config_file)
        except json.JSONDecodeError as error:
            print(f"Error getting json file: {error}")
        except FileNotFoundError:
            print(f"Config file not found at {config_path}")
        return config
    
    def kelvin_to_celsius(kelvin: float) -> float:
        celsius = kelvin - 273.15
        return celsius
