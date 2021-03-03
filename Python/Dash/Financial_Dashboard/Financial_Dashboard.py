import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dcc
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries
from dash.dependencies import Input, Output


app = dash.Dash(__name__)


# Obtain Data


#App Layout
app.layout = html.Div([
    html.Br(),
    html.H1("Financial Dashboard", style={'text-align': 'center'}),
    html.Br(),
])



#The callback
@app.callback([])

def update_graph():
    pass



#Launch App
if __name__ == '__main__':
    app.run_server(debug=True)