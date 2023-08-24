import pandas
from dash import Dash, html
from database import MainDatabase 

def get_data():
    tables = MainDatabase.get_db_tables()
    dataframes = {}

    for table in tables:
        table_name = table[0]
        quary = f"SELECT * from {table_name}"
        # dataframe = 


class Webpage():
    def __init__(self, host, port) -> None:
        app = Dash(__name__)

        app.layout = html.Div(
            [
                html.Div(children="Temperature data"),
                
            ]
        )

        app.run(host='0.0.0.0', port=8050, debug=True)


Webpage()


# import requests
# from dash import Dash, html, dash_table, dcc
# import pandas as pd
# import plotly.express as px
# import config

#     # Compare temperature
#     dcc.Graph(figure=px.line(df, x="datetime",
#                              y=["temperature", "ext_temperature"],
#                              labels={"datetime": "Date and time",
#                                      "value": "Temperature (°C)"},
#                              title="Interior and exterior temperature "
#                                    "comparison"
#                              )),

#     # Compare humidity
#     dcc.Graph(figure=px.line(df, x="datetime",
#                              y=["humidity", "ext_humidity"],
#                              labels={"datetime": "Date and time",
#                                      "value": "Humidity %"},
#                              title="Interior and exterior humidity "
#                                    "comparison"
#                              )),

#     dash_table.DataTable(data=df.to_dict("records"), page_size=10),
# ])

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8050, debug=True)