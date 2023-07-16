import sqlite3
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

connection = sqlite3.Connection('ht.db')
df = pd.read_sql('SELECT * FROM ht_table', connection)

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Temperature data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.line(df, x='datetime', y='temperature')),
    dcc.Graph(figure=px.line(df, x='datetime', y='humidity'))
])

if __name__ == '__main__':
    app.run(debug=True)
