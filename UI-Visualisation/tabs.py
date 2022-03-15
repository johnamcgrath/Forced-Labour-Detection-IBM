import dash
from dash import html
import plotly.graph_objects as go
from dash import dcc
import plotly.express as px
from dash import Dash
from dash.dependencies import Input, Output

from app import df

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Human Trafficking - Job Advertisement', style={'color': 'purple', 'textAlign': 'center'}),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='General Information', value='tab-1'),
        dcc.Tab(label='Specific variable', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div([
                html.H5('graph example 1'),
                dcc.Graph(id='g1', figure={'data': [{'y': [1, 2, 3], 'line':dict(color='green')}]})
            ], className="six columns"),

            html.Div([
                html.H5('graph example 2'),
                dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
            ], className="six columns"),

            html.H6('This is where we will include some facts about the overall figures. It will include countries '
                    'with biggest risk ect.'),
        ])

    elif tab == 'tab-2':
        return html.Div([
            html.H5('Industry'),
            dcc.Dropdown(id='dropdown',
                         options=[
                             {'label': 'Hospitality', 'value': 'H'},
                             {'label': 'Engineering', 'value': 'E'},
                         ],
                         value='H'),
            html.H3('           '),
            html.H5('Country'),
            dcc.Dropdown(id='dropdown2',
                         options=[
                             {'label': 'United Kingdom', 'value': 'UK'},
                             {'label': 'Ireland', 'value': 'I'},
                         ],
                         value='I')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
