import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import threading
import time

from database import ClimateDatabase

app = dash.Dash(__name__)

class TemperatureDashboard:
    def __init__(self):
        self.app = app
        self.app.layout = html.Div([
            dcc.Graph(id="data-graph"),
            dcc.Interval(
                id='interval-component',
                interval=10000,  # in milliseconds
                n_intervals=0
            )
        ])

        self.lock = threading.Lock()
        self.dataframe = None

        self.app.callback(
            Output("data-graph", "figure"),
            Input("interval-component", "n_intervals")
        )(self.update_graph)

        self.update_thread = threading.Thread(target=self.update_data)
        self.update_thread.daemon = True
        self.update_thread.start()

    def run(self):
        self.app.run_server() # Set debug=True if needed

    def update_data(self):
        while True:
            climate_database = ClimateDatabase("climate")  # Create a new connection in each thread
            with self.lock:
                self.dataframe = climate_database.get_db_data()
            time.sleep(60)  # Update data every 60 seconds

    def update_graph(self, n):
        with self.lock:
            dataframe = self.dataframe
        if dataframe is None:
            return {}

        subplots = []

        for table_name, df in dataframe.items():
            subplot = {
                "x": df["datetime"],
                "y": df["temperature"],
                "type": "line",
                "name": f"Temperature - {table_name}"
            }
            subplots.append(subplot)

        figure = {
            "data": subplots, 
            "layout": {
                "title": "Temperature data",
                "xaxis": {"title": "Data Time"},
                "yaxis": {"title": "Value"}
            }
        }

        return figure

if __name__ == "__main__":
    dashboard = TemperatureDashboard()
    dashboard.run()