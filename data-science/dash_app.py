from dash import Dash, html, dcc, dash_table, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash()

data = pd.read_csv('rad_2008_15min.csv', low_memory=False)


app.layout = [
    html.H1(children='Fahrradfahrer München', style={'textAlign':'center'}),
    html.Hr(),
    dcc.Dropdown(
        options=[
            {'label': 'Arnulfstraße', 'value': 'Arnulf'},
            {'label': 'Erhardtstraße', 'value': 'Erhardt'},
            {'label': 'Hirschgarten', 'value': 'Hirsch'},
            {'label': 'Bad-Kreuther-Straße', 'value': 'Kreuther'},
            {'label': 'Margaretenstraße', 'value': 'Margareten'},
            {'label': 'Olympiapark', 'value': 'Olympia'},
            {'label': 'Gesamt', 'value': ''} # empty value to filter for all
        ],
        value='Gesamt',
        id='location'
    ),
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
    dash_table.DataTable(data=data.to_dict('records'), page_size=100, id='table'),
    dcc.Graph(figure=px.histogram(data, x='datum', y='gesamt', histfunc='avg'), id='graph')
]

@callback(
    Output(component_id='table', component_property='data'),
    Input(component_id='location', component_property='value'),
    Input(component_id='year', component_property='value')
)
def update_table(location, year):
    data = pd.read_csv(f'rad_{year}_15min.csv', low_memory=False)
    if location:
        return data[data['zaehlstelle'].str.contains(location)].to_dict('records')
    else:
        return data.to_dict('records')

@callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='location', component_property='value'),
    Input(component_id='year', component_property='value')
)
def update_graph(location, year):
    data = pd.read_csv(f'rad_{year}_15min.csv', low_memory=False)
    if location:
        return px.histogram(data[data['zaehlstelle'].str.contains(location)], x='datum', y='gesamt', histfunc='sum')
    else:
        return px.histogram(data, x='datum', y='gesamt', histfunc='sum')

if __name__ == '__main__':
    app.run(debug=True)