import json


class Configuration():
    def __init__(self, config_path):
        with open(config_path) as config_file:
            self.config = json.load(config_file)
    

    def find_raspberry(self):
        raspberrys = self.config["raspberry_ip"]
        for raspberry in raspberrys:
            data = raspberrys[raspberry]


class Data():
    def get_data(self, ip_port):
        # For each ip, get data. Log to object???? 

        


my_config = Configuration("config.json")


print(my_config.get_data())

# Class. Config. Per Rasppi, create objects. 
# Get data call
