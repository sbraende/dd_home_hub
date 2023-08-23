import time
import database
import exterior_climate
import interior_climate


class Database():
    def __init__(self) -> None:
        self.climate_database = database.Main("climate")
        self.exterior_instance = exterior_climate.OpenWeather()
        self.interior_instance = interior_climate.Setup()

    def write_data(self):
        while True:
            self.climate_database.write_data(self.exterior_instance.table_name,
                                            self.exterior_instance.get_weather())
            self.climate_database.write_interior_data(self.interior_instance.raspberry_instances)
            time.sleep(120)  # Set to no lower than 120 seconds


if __name__ == '__main__':
    main_database = Database()
    main_database.write_data()
