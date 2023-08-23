import sqlite3
from datetime import datetime
from pathlib import Path


class Main():
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
    
    def make_table(self, table_name: str, data: dict):
        columns_names = ", ".join(data.keys())
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_names})")

    def write_data(self, table_name: str, data: dict):
        columns_names = ", ".join(data.keys())
        # Make table here? 
        data_points = ", ".join(["?" for _ in data])
        data_values = list(data.values())
        self.cursor.execute(f"INSERT INTO {table_name} ({columns_names}) VALUES ({data_points})", data_values)
        self.connection.commit()
        self.connection.close()
