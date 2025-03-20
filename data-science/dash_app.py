import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, dash_table, callback, Output, Input

app = Dash()

data = pd.read_csv('buffer/rad_2008_15min.csv', low_memory=False)
data_days = pd.read_csv('buffer/rad_2008.csv', low_memory=False)

app.layout = [
    html.Div(
        [
            html.H1(children='Fahrradfahrer München', style={'textAlign': 'center'}),
            html.Hr(),
            html.Div(
                [
                    dcc.Dropdown(
                        options=[
                            {'label': 'Arnulfstraße', 'value': 'Arnulf'},
                            {'label': 'Erhardtstraße', 'value': 'Erhardt'},
                            {'label': 'Hirschgarten', 'value': 'Hirsch'},
                            {'label': 'Bad-Kreuther-Straße', 'value': 'Kreuther'},
                            {'label': 'Margaretenstraße', 'value': 'Margareten'},
                            {'label': 'Olympiapark', 'value': 'Olympia'},
                            {'label': 'Gesamt', 'value': ''}  # empty value to filter for all
                        ],
                        value='Gesamt',
                        id='location'
                    ),
                ],
                style={'width': '98%', 'margin': '0px auto'}
            ),
            html.Div(
                [
                    dcc.Dropdown(
                        options=[
                            {'label': '2008', 'value': '2008'},
                            {'label': '2009', 'value': '2009'},
                            {'label': '2010', 'value': '2010'},
                            {'label': '2011', 'value': '2011'},
                            {'label': '2012', 'value': '2012'},
                            {'label': '2013', 'value': '2013'},
                            {'label': '2014', 'value': '2014'},
                            {'label': '2015', 'value': '2015'},
                            {'label': '2016', 'value': '2016'},
                            {'label': '2017', 'value': '2017'},
                            {'label': '2018', 'value': '2018'},
                            {'label': '2019', 'value': '2019'},
                            {'label': '2020', 'value': '2020'},
                            {'label': '2021', 'value': '2021'},
                            {'label': '2022', 'value': '2022'},
                            {'label': '2023', 'value': '2023'},
                            {'label': '2024', 'value': '2024'},
                        ],
                        value='2008',
                        id='year'
                    ),
                ],
                style={'width': '98%', 'margin': '0px auto'}
            ),
            html.H2(
                children=f'Übersicht Fahrradfahrer',
                style={'textAlign': 'center'}),
            html.Div(
                [
                    dcc.Graph(
                        figure=px.histogram(data, x='datum', y='gesamt', histfunc='sum'),
                        id='graph_histo'
                    ),
                ],
                style={'width': '100%', 'margin': '0px auto'}
            ),
            html.Br(),
            html.Hr(),
            html.H2(
                children='Vergleich Messstationen',
                style={'textAlign': 'center'}
            ),
            html.Div(
                [
                    dcc.Graph(
                        figure=px.line(data_days, x='datum', y='gesamt', color='zaehlstelle'),
                        id='graph_line'
                    ),
                ],
                style={'width': '100%', 'margin': '0px auto'}
            ),
            html.Hr(),
            html.H2(
                children='Tabelle',
                style={'textAlign': 'center'}
            ),
            html.Div(
                [
                    dash_table.DataTable(
                        data=data.to_dict('records'),
                        page_size=80, id='table',
                        hidden_columns=[
                            # 'kommentar',
                            'line_number',
                        ],
                    ),
                ],
                style={'width': '98%', 'margin': '0px auto'}
            ),
        ],
        style={'width': '98%', 'margin': '0px auto'},
    ),
]


@callback(
    Output(component_id='table', component_property='data'),
    Input(component_id='location', component_property='value'),
    Input(component_id='year', component_property='value')
)
def update_table(location, year):
    data = pd.read_csv(f'buffer/rad_{year}_15min.csv', low_memory=False)
    if location:
        return data[data['zaehlstelle'].str.contains(location)].to_dict('records')
    else:
        return data.to_dict('records')


@callback(
    Output(component_id='graph_histo', component_property='figure'),
    Input(component_id='location', component_property='value'),
    Input(component_id='year', component_property='value')
)
def update_histo_graph(location, year):
    data = pd.read_csv(f'buffer/rad_{year}_15min.csv', low_memory=False)
    if location:
        return px.histogram(data[data['zaehlstelle'].str.contains(location)], x='datum', y='gesamt', histfunc='sum')
    else:
        return px.histogram(data, x='datum', y='gesamt', histfunc='sum')


@callback(
    Output(component_id='graph_line', component_property='figure'),
    Input(component_id='year', component_property='value'),
)
def update_line_graph(year):
    data_days = pd.read_csv(f'buffer/rad_{year}.csv', low_memory=False)
    return px.line(data_days, x='datum', y='gesamt', color='zaehlstelle')


if __name__ == '__main__':
    app.run(debug=True)
