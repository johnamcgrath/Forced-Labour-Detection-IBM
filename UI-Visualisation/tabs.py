import json
import dash
from dash import html
import plotly.graph_objects as go
from dash import dcc
import plotly.express as px
from dash import Dash
from dash.dependencies import Input, Output
from app import df

colors = {
    'background': '#1F2833',
    'heading': '#66FCF1',
    'tabColor': '#1F2833',
    'tabBarColor': '#45A29E',
    'graphColor': '#2E5984'
}

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #66FCF1',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #45A29E',
    'borderBottom': '1px solid #45A29E',
    'backgroundColor': '#45A29E',
    'color': '#66FCF1',
    'padding': '6px'
}

json_file_path = "nlp-output.json"
with open(json_file_path) as f:
    data = json.load(f)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries'  # Represent only large countries

figure=px.pie(df, values='pop', names='country', title='Population of European continent')

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1('Human Trafficking - Job Advertisement', style={'color': colors['heading'], 'textAlign': 'center'}),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='General Information', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Specific variable', value='tab-2', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([

            html.Div([
                html.H5('Graph Example 1', style={'color': colors['tabBarColor'], 'textAlign': 'center'}),
                dcc.Graph(id='g1',

                          figure={'layout': {
                              'plot_bgcolor': colors['graphColor'],
                              'paper_bgcolor': colors['background'],
                              'font': {
                                  'color': colors['tabBarColor']
                              }
                          },
                              'data': [{'y': [1, 2, 3], 'line': colors['tabBarColor']}]})
            ], className="six columns"),

            html.Div([
                html.H5('Graph Example 2', style={'color': colors['tabBarColor'], 'textAlign': 'center'}),
                dcc.Graph(id='g2',
                          figure=px.pie(df, values='pop', names='country', title='Population of European continent')
                          )
            ], className="six columns"),

            dcc.DatePickerRange(
                start_date_placeholder_text="Start Period",
                end_date_placeholder_text="End Period",
                calendar_orientation='vertical',
            ),

        ])

    elif tab == 'tab-2':
        return html.Div([

            html.H5('Country', style={'color': colors['tabBarColor']}),
            dcc.Dropdown(id='dropdown2',
                         options=[
                             {'label': 'United Kingdom', 'value': 'UK'},
                             {'label': 'Ireland', 'value': 'I'},
                         ],
                         value='I'),
            html.H3('           '),
            html.H5('Industry', style={'color': colors['tabBarColor']}),
            dcc.Dropdown(id='dropdown',
                         options=[
                             {'label': 'Hospitality', 'value': 'H'},
                             {'label': 'Engineering', 'value': 'E'},
                         ],
                         value='H'),
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
