import json


class Configuration():
    def __init__(self, config_path):
        try:
            with open(config_path) as config_file:
                self.config = json.load(config_file)
        except json.JSONDecodeError as error:
            print(f"Error getting json file: {error}")
        except FileNotFoundError:
            print(f"Config file not found at {config_path}")

    def find_raspberry(self):
        raspberrys = self.config["raspberry_ip"]
        for raspberry in raspberrys:
            data = raspberrys[raspberry]


class Data():
    def get_data(self, ip_port):
        # For each ip, get data. Log to object???? 

        
        except sqlite3.Error as error:
            print(f"Error while initializing the database: {error}")
    

my_config = Configuration("config.json")


print(my_config.get_data())

# Class. Config. Per Rasppi, create objects. 
# Get data call
