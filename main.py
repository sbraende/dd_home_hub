import database
import exterior_climate
import interior_climate


class Database():
    def __init__(self) -> None:
        self.climate_database = database.Config("climate")
        self.interior_instance = interior_climate.Config()
        self.exterior_instance = exterior_climate.OpenWeather()

        self.interior_table = self.climate_database.make_table(
            "Interior_climate", self.interior_instance.get_interior_climate())
        self.exterior_table = self.climate_database.make_table(
            "Exterior_climate", self.exterior_instance.get_weather())

    def log_data(self):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    Database()

# Make main function
    # Create instance of needed classes

    # Thread - gather and log exterior temperature
    # Thread start

    # Thread - gather and log interior temperature
    # Thread start

    # Start dashboard 
