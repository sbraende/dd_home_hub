import sqlite3
from datetime import datetime
from pathlib import Path


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
        self.cursor.execute(f"CREATE TABLE {table_name} ({columns_formatted})")
        print(f"Table {table_name} created")

    def check_table(self, table_name: str):
        return bool(self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'").fetchone())


class ReadWriteData():
    def __init__(self):         ### Do I need this?? 
        self.test = "test"      ### Do I need this??    

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
my_db.make_table("livingroom", data_handler.get_interior_climate())
data_handler.write_data(data_handler.get_interior_climate(), "livingroom", my_db.cursor)