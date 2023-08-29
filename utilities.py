import json
from pathlib import Path


class HelperFunctions():
    def open_config(config_path: str) -> dict:
        path = Path(config_path)
        if not path.exists():
            raise FileNotFoundError(f"Cannot find the config file: {config_path}")
        try:
            with open(config_path) as config_file:
                config = json.load(config_file)
                return config
        except json.JSONDecodeError as error:
            raise ValueError(f"Cannot decode JSON in config file: {error}")


    def kelvin_to_celsius(kelvin: float) -> float:
        celsius = kelvin - 273.15
        return celsius
