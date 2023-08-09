import requests
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px
import config

api_url = f"http://{config.userdata['raspberry_ip']}:5000/database"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    columns_names = data["columns"]
    data_rows = data["data"]
    df = pd.DataFrame(data_rows, columns=columns_names)
else:
    print("Failed to retrieve data from API.")

# print(df)

app = Dash(__name__)

app.layout = html.Div([
    # html.Div(children="Temperature data"),

    # Compare temperature
    dcc.Graph(figure=px.line(df, x="datetime",
                             y=["temperature", "ext_temperature"],
                             labels={"datetime": "Date and time",
                                     "value": "Temperature (°C)"},
                             title="Interior and exterior temperature "
                                   "comparison"
                             )),

    # Compare humidity
    dcc.Graph(figure=px.line(df, x="datetime",
                             y=["humidity", "ext_humidity"],
                             labels={"datetime": "Date and time",
                                     "value": "Humidity %"},
                             title="Interior and exterior humidity "
                                   "comparison"
                             )),

    dash_table.DataTable(data=df.to_dict("records"), page_size=10),
])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)
