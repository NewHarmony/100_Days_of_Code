# Credit: Based on a tutorial from Charming Data https://www.youtube.com/watch?v=hSPmj7mK6ng&list=PLHezTAVBPWVM3vwd-GY8907IsryL5zYYm&index=34

import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Loading Data
df = pd.read_csv("intro_bees.csv")
print(df[:5])
df = df.groupby(['State', 'ANSI','Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])
bee_killers = df["Affected by"].unique().tolist()
print(bee_killers)
states = df["State"].unique().tolist()
print(states)

#App Layout
app.layout = html.Div([
    html.H1("Bee Web Application Dashboard", style={'text-align': 'center'}),
    html.Br(),
    html.Br(),
    html.Div(
        [dcc.Dropdown(id="slct_year", 
                    options=[
                        {"label": "2015", "value": 2015},
                        {"label": "2016", "value": 2016},
                        {"label": "2017", "value": 2017},
                        {"label": "2018", "value": 2018}],
                    multi=False,
                    value=2015,
                    style={'width': "40%",'color':'darkgray'}
                    ),
    html.Div(id='output_container', children=[])],
    style={'display':'flex', 'text-align': 'left'} 
    ),
    html.Br(),

    html.H2("Colonies Affected By Varroa_mites", style={'text-align': 'left'}), 

    dcc.Graph(id='my_bee_map', figure={}),
    
    html.Br(), 
    html.H2("Colonies Affected By Pesticides", style={'text-align': 'left'}),
    html.Div(
        [dcc.Graph(id='my_bee_map2', figure={}),
        dcc.Graph(id='my_bee_map3', figure={})], style={'display': 'flex', 'width':'100%'}
    ),
    
    html.Br(), 
    html.H2("Problems Known To Affect Bess", style={'text-align': 'left'}),
    html.Br(),
    html.Div(
        [dcc.Dropdown(id="slct_issue", 
                    options=[{"label": issue, "value": issue} for issue in bee_killers],
                    multi=False,
                    value="Pesticides",
                    style={'width': "40%",'color':'darkgray'}
                    ),
        dcc.Dropdown(id="slct_state", 
                    options=[
                        {"label": state, "value": state} for state in states],
                    multi=True,
                    value=states[:2],
                    style={'width': "40%",'color':'darkgray'}
                    )], 
        style={'display': 'flex', 'width':'100%'}
        ),

    html.Div(dcc.Graph(id='line_chart', figure={})
    )
], style={'background-color':'black', 'color':'white', "padding":"5px"})

#The callback
@app.callback(
    [Output(component_id='output_container', component_property='children'),
    Output(component_id='my_bee_map', component_property='figure'),
    Output(component_id='my_bee_map2', component_property='figure'),
    Output(component_id='my_bee_map3', component_property='figure'),
    Output(component_id='line_chart', component_property='figure')],
    [Input(component_id='slct_year', component_property='value'),
    Input(component_id='slct_issue', component_property='value'),
    Input(component_id='slct_state', component_property='value'),
    ]
    )

def update_graph(option_slctd, issue, states_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "Selected Year: {}".format(option_slctd)

    df_copy = df.copy()
    df_copy = df_copy[df_copy["Year"] == option_slctd]
    df_copy = df_copy[df_copy["Affected by"] == "Varroa_mites"]

    #Plotly
    fig = px.choropleth(
        data_frame = df_copy,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )
    df_copy = df.copy()
    df_copy = df_copy[df_copy["Year"] == option_slctd]
    df_copy = df_copy[df_copy["Affected by"] == "Pesticides"]

    fig2 = px.choropleth(
        data_frame = df_copy,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
        )

    fig3 = px.bar(df_copy, x='state_code', y='Pct of Colonies Impacted')
    # fig.show()
    
    df_copy = df.copy()
    df_copy = df_copy[df_copy["Affected by"] == issue]
    df_copy = df_copy[df_copy["State"].isin(states_slctd)]


    fig_linechart = px.line(df_copy, x='Year', y='Pct of Colonies Impacted', color = 'State',template='plotly_dark')

    
    return container, fig, fig2, fig3, fig_linechart

if __name__ == '__main__':
    app.run_server(debug=True)