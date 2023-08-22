import sqlite3
from pathlib import Path
import exterior_climate


class Config():
    def __init__(self, db_name: str):
        self.name = db_name
        self.filename = f"{self.name}.db"
        self.path = Path(self.filename)

        if not self.path.exists():
            print(f"File not on disk. Creating {self.filename}")

        try:
            self.connection = sqlite3.connect(self.filename)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as error:
            print(f"Error while initializing the database: {error}")
    
    def make_table(self, table_name: str, columns: dict):
        columns_formatted = ", ".join(columns.keys())
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_formatted})")


class ReadWriteData(): 
    def get_interior_climate(self):
        data = {
            "room": "roomname",  # Get data from interior climate
            "humidity": "55",     # Get data from interior climate
            "temperature": "24"   # Get data from interior climate
        }
        return data

    def write_data(self, data: dict, table_name: str, cursor: object):
        data_columns = ", ".join(data.keys())
        data_points = ", ".join(["?" for _ in data])
        data_values = list(data.values())

        cursor.execute(f"INSERT INTO {table_name} ({data_columns}) VALUES ({data_points})", data_values)


my_db = Config("climate")
data_handler = ReadWriteData()
ext_weather = exterior_climate.OpenWeather("config.json")

my_db.make_table("exterior_weather", ext_weather.get_weather())
data_handler.write_data(ext_weather.get_weather(), "exterior_weather", my_db.cursor)

my_db.connection.commit()  # Don't forget to commit changes
my_db.connection.close()   # Don't forget to close the connection


# my_db.make_table("livingroom", data_handler.get_interior_climate())
# data_handler.write_data(data_handler.get_interior_climate(), "livingroom", my_db.cursor)
