import json
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd
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

with open('nlp-output2.json') as json_file:
    data = json.load(json_file)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

risk_score = [i['risk_score'] for i in data["ads"]]
ad_id = [i['ad_id'] for i in data["ads"]]
industry = [i['industry'] for i in data["ads"]]
country = [i['country'] for i in data["ads"]]

df2 = pd.DataFrame({'ad id': ad_id, 'risk score': risk_score})
fig2 = px.bar(df2, x="ad id", y="risk score")

df3 = pd.DataFrame({'industry' : industry})
df4 = pd.DataFrame({'country' : country})

df5 = pd.DataFrame({'risk score':risk_score, 'country' : country})

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries'  # Represent only large countries
figure = px.pie(df, values='pop', names='country', title='Population of European continent')


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
                          figure=px.bar(df2,x = "ad id", y="risk score", title='Risk score Bar Chart', color = 'risk score', color_continuous_scale=px.colors.sequential.Viridis)
                          )
            ], className="six columns"),

            html.Div([
                html.H5('Graph Example 2', style={'color': colors['tabBarColor'], 'textAlign': 'center'}),
                dcc.Graph(id='g2',
                          figure=px.pie(df5, values='risk score', names='country', color_discrete_sequence=px.colors.sequential.RdBu)
                          )
            ], className="six columns"),

            html.H5('sp', style={'color': colors['background']}),

            dcc.DatePickerRange(
                start_date_placeholder_text="Start Period",
                end_date_placeholder_text="End Period",
                calendar_orientation='vertical',
            ),
            html.H3('       heelo    ', style={'color': colors['background']}),
            html.H3('      hi     ', style={'color': colors['background']}),
            html.H3('     bonjour      ', style={'color': colors['background']}),
            html.H3('     hola      ', style={'color': colors['background']}),
            html.H3('   hi        ', style={'color': colors['background']}),
            html.H3('    h       ', style={'color': colors['background']}),
            html.H3('     h      ', style={'color': colors['background']}),
            html.H3('     h      ', style={'color': colors['background']}),
            html.H3('       h    ', style={'color': colors['background']}),
            html.H3('      h     ', style={'color': colors['background']}),
            html.H3('     h      ', style={'color': colors['background']}),
            html.H3('     h      ', style={'color': colors['background']}),

        ])

    elif tab == 'tab-2':
        return html.Div([

            html.H5('sp', style={'color': colors['background']}),

            html.H5('Industry', style={'color': colors['tabBarColor']}),
            html.H5('     ', style={'color': colors['background']}),
            dcc.Dropdown(df3.industry.unique(), id='pandas-dropdown-1'),

            html.H3('   ', style={'color': colors['background']}),

            html.H5('Country', style={'color': colors['tabBarColor']}),
            html.H5('     ', style={'color': colors['background']}),
            dcc.Dropdown(df4.country.unique(), id='pandas-dropdown-2'),
            html.Div(id='pandas-output-container-1'),

            ]),




if __name__ == '__main__':
    app.run_server(debug=True)
