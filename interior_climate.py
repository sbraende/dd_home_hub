from datetime import datetime
import requests
import utilities


class Setup():
    def __init__(self):
        self.config = utilities.HelperFunctions.open_config("config.json")
        # self.table_names = ["raspberry01", "raspberry02"]  ## For each raspbeery get raspberry name
        self.raspberry_instances = self.get_raspberrys()

    def get_raspberrys(self) -> list:
        raspberry_instances = []
        raspberrys_in_json = self.config.get("interior_climate", {}).get("dd_home_server_api", {}).items()
        for raspberry_name, address_port in raspberrys_in_json:
            raspberry_instance = Raspberry(raspberry_name, address_port)
            raspberry_instances.append(raspberry_instance)
        return raspberry_instances


class Raspberry():
    def __init__(self, name, address_port) -> object:
        self.name = name
        self.address_port = address_port
        self.url = f"http://{address_port}/data"

    def get_data(self): 
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            data.update({"datetime": str(datetime.now())})
            return data
        else:
            print("Failed to retrieve data from API.")
