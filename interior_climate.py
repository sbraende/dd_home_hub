import json
import requests


class Config():
    def __init__(self, config_path: str):
        config = self.open_config(config_path)

        raspberry_instances = []
        
        for raspberry_name, address_port in config.get("interior_climate", {}), config.get("dd_home_server_api", {}).items():
            address = f"http://{address_port}/data"
            raspberry_instance = Raspberry(address)
            raspberry_instances.append(raspberry_instance)

        for raspberry_instance in raspberry_instances:
            print(raspberry_instance.address)


    def open_config(self, config_path: str) -> dict:
        try:
            with open(config_path) as config_file:
                config = json.load(config_file)
        except json.JSONDecodeError as error:
            print(f"Error getting json file: {error}")
        except FileNotFoundError:
            print(f"Config file not found at {config_path}")
        return config


class Raspberry():
    def __init__(self, address) -> object:
        # self.name = name
        self.address = address

        # self.url = str
        # self.data = list


my_config = Config("config.json")




    # def get_data(self) -> object:
    #     for call in self.api_urls:
    #         response = requests.get(data)
    #         if response.status_code == 200:
    #             data = response.json()
    #             return data
    #         else:
    #             print("Failed to retrieve data from API.")


        # raspberry_dict = self.config["interior_climate"]["dd_home_server_api"]
        # api_urls = []
        # for raspberry_name, address_port in raspberry_dict.items():
        #     api_url = f"http://{address_port}/data"
        #     api_urls.append(api_url)
        # return api_urls