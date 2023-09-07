import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import json

from utilities import HelperFunctions
from database import MainDatabase

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="data-graph"),
    dcc.Interval(
        id='interval-component',
        interval=10000,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(
    Output("data-graph", "figure"),
    Input("interval-component", "n_intervals") # add interval component
)
def update_graph(n):
    climate_database = MainDatabase("climate")
    dataframe = climate_database.get_db_data()

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
    app.run_server(debug=True)



# class WebpApp():
#     def __init__(self) -> None:
#         self.config = HelperFunctions.open_config("config.json")
        
#         self.host = self.get_host()
#         self.port = self.get_port()

#         self.climate_database = MainDatabase("climate")  # Get this into the main app
#         self.df = self.climate_database.get_db_data()    # Reference at top 

#         print(self.df)

#     def get_host(self):
#         return self.config["website_api"]["host"]

#     def get_port(self):
#         return self.config["website_api"]["port"]

#     def run(self):
#         pass


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



# self.app.run(host="0.0.0.0", port=8500, debug=True)




# def main():
#     webpage = WebpApp()
#     webpage.run()


# if __name__ == "__main__":
#     main()
