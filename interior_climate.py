import requests
import utilities


class Config():
    def __init__(self):
        self.config = utilities.HelperFunctions.open_config("config.json")
        self.table_names = ["raspberry01", "raspberry02"]  ## For each raspbeery get raspberry name

    def get_interior_climate(self):
        for raspberry in self.get_raspberrys():
            data = self.get_url_data(raspberry.url)
            # write data to database?
            return data

    def get_raspberrys(self) -> object:
        raspberry_instances = []
        raspberrys_in_json = self.config.get("interior_climate", {}).get("dd_home_server_api", {}).items()
        for raspberry_name, address_port in raspberrys_in_json:
            raspberry_instance = Raspberry(raspberry_name, address_port)
            raspberry_instances.append(raspberry_instance)
        return raspberry_instances

    def get_url_data(self, url): 
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Failed to retrieve data from API.")

class Raspberry():
    def __init__(self, name, address_port) -> object:
        self.name = name
        self.address_port = address_port
        self.url = f"http://{address_port}/data"

        