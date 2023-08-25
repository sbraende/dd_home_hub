import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import json

from utilities import HelperFunctions
from database import MainDatabase


class DataPrep():


class WebpApp():
    def __init__(self) -> None:
        self.config = HelperFunctions.open_config("config.json")
        
        self.host = self.get_host()
        self.port = self.get_port()

        main_database = MainDatabase("climate")  # Get this into the main app
        self.df = main_database.get_db_data()    # Reference at top 
        
        formatted_data = json.dumps(self.df, indent=4)
        print(formatted_data)


        # self.app = Dash(__name__)

        # self.app.layout = html.Div([
        #         html.Div(id="temperature-graph"),
        #     ])

        # self.app.callback(
        #     Output("temperature-graph", "figure"),
        #     # Input("interval-component", "n_intervals") 
        # )

        # def update_graph(n):



                # # Temperature graph
                # dcc.Graph(figure=px.line(self.df,
                #                          x="datetime",
                #                          y=["temperature", "ext_temperature"],
                #                          labels={"datetime": "Date and time",
                #                                 "value": "Temperature (°C)"},
                #                          title="Interior and exterior temperature "
                #                             "comparison"
                #                         ))


    def get_host(self):
        return self.config["website_api"]["host"]

    def get_port(self):
        return self.config["website_api"]["port"]

    def run(self):
        self.app.run(host=self.host, port=int(self.port), debug=True)


def main():
    webpage = WebpApp()
    # webpage.run()


if __name__ == "__main__":
    main()
