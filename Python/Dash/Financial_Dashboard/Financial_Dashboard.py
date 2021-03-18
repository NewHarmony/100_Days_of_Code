import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries
import yfinance as yf
from dash.dependencies import Input, Output


app = dash.Dash(__name__)


# Obtain Data
# ticker = ['JNJ', 'PFE', 'UNH', 'MRK', 'NVS']
# start = "1997-01-01"
# end = "2020-12-31"
# med_stocks = yf.download(ticker, start= start, end = end )[["Open", "High", "Low","Close","Adj Close"]]
# print(med_stocks)
# med_stocks.to_csv("med_stocks.csv")
# print(med_stocks.describe())
# print(med_stocks.index)

med_stocks = pd.read_csv("med_stocks.csv", header = [0,1], index_col= [0], parse_dates= [0])
print(med_stocks)
print(med_stocks.describe())
print(med_stocks.index)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
meta_tags=[{'name': 'viewport',
            'content': 'width = device-width, initial-scaled=1.0'}]
)



#App Layout
app.layout = html.Div([
    html.Br(),
    html.H1("Financial Dashboard", style={'text-align': 'center'}),
    html.Br(),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(
                        src="JNJ.png",
                        top=True,
                        style={"width":"10px"},
                        ),
                    
                ])
            ])
        ])
    ])
])



#The callback
# @app.callback([])

# def update_graph():
#     pass



#Launch App
if __name__ == '__main__':
    app.run_server(debug=True)