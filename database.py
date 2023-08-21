import sqlite3
from pathlib import Path


class DBConfig():
    def __init__(self, db_name: str, columns: list):
        self.name = db_name
        self.columns = columns
        self.filename = f"{self.name}.db"
        self.path = Path(self.filename)
        
        try: 
            if self.path.exists():
                self.connection = sqlite3.connect(self.filename)
                self.cursor = self.connection.cursor()
            else:
                self.make_db()
        except sqlite3.Error as error:
            print(f"Error while initializing the database: {error}")

    def make_db(self):
        try:
            print(f"File not on disk. Creating {self.filename}")
            self.connection = sqlite3.connect(self.filename)
            self.cursor = self.connection.cursor()
            columns_formatted = ", ".join(self.columns)  # Formatting for table
            self.cursor.execute(f"CREATE TABLE {self.name}_table ({columns_formatted})")
        except sqlite3.Error as error:
            print(f"Error while creating the database {error}")


my_db = DBConfig("humidtemp", ["one", "two"])
print(my_db.connection.cursor)