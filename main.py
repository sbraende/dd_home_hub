import database
import exterior_climate
import interior_climate


class Database():
    def __init__(self) -> None:
        self.climate_database = database.Main("climate")
        self.interior_instance = interior_climate.Config()
        self.exterior_instance = exterior_climate.OpenWeather()

        self.climate_database.make_table(self.interior_instance.table_names[0],
                                         self.interior_instance.get_interior_climate())
        
        self.climate_database.make_table(self.exterior_instance.table_names[0],
                                         self.exterior_instance.get_weather())

    def log_data(self):
    #     self.climate_database.write_data("interior_climate", 
    #                                      self.exterior_instance.get_weather())
        self.climate_database.write_data(self.exterior_instance.table_names[0],  # Name of table
                                         self.exterior_instance.get_weather())
        

    def run(self):
        pass


if __name__ == '__main__':
    main_database = Database()
    main_database.log_data()

