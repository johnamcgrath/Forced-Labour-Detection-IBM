import json
from dash import html, callback_context
from dash import dcc
import plotly.express as px
import pandas as pd
from dash import Dash
from dash.dependencies import Input, Output
from app import df


colors = {
    'background': '#000000',
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
app.css.append_css({'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'})

risk_score = [i['risk_score'] for i in data["ads"]]
ad_id = [i['ad_id'] for i in data["ads"]]
industry = [i['industry'] for i in data["ads"]]
country = [i['country'] for i in data["ads"]]

df = pd.DataFrame({'ad id': ad_id, 'risk score': risk_score,'industry' : industry,'country' : country})
fig2 = px.bar(df, x="ad id", y="risk score")


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.A([
        html.Img(
            src='https://i.pinimg.com/736x/21/d6/7f/21d67f1d6b3be5bb2e39395311c77fc6.jpg',
            style={
                'height': '2%',
                'width': '2%',
                'float': 'right',
                'position': 'right',
                'padding-top': 0,
                'padding-right': 0
            })
    ], href='https://www.instagram.com/accounts/login/?next=/traffikanalysishub/'),
    html.A([
        html.Img(
            src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARUAAAC2CAMAAADAz+kkAAAAz1BMVEUAAAD////bJyTKHSDGGx/gKibZJiTCGR7NHyHVJCPHHB/aJyTfKibjLCbQISHpLiigHxv6+fkzCAirFBqUHBnlhYTLAACaHhry7e3p5+fn39/gg4SkExkTAgJCDAqKGhdyFRNaEA4eBQTYGBXVAAA0CQjLDhGYEhcoBgZLDgxdEQ9qFBF5FxSBGRVlExE7Cgm7JCDAJSDuvr7jn57ekZHYFRLm1tbcdXTmzMzca2rbYWDkwMDZVlXZS0risrLXQD/WNTXyy8v22dn45ubij4+BFthxAAAED0lEQVR4nO3ca3eaShSHcQRRtEBUqNZLBKvxEkUxJr03Sdvz/T/TAdM2djVndfZ4mOmO/9+rJEtY2c8aCKLRMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADgL3I+vxguRpfrZbxaJUkUhWHY6XQaP2RfZz8JoyRJVvFyfTlaDDet17p/6QJs1knYCNKtU3PP5NkVv75NG50oXuge6HhxejCZd5TH/VgR69Wzco8s8Z+BGrpHk7ctpsm+i8v0QJrXiouSd1nqHlDGeaXIJnmWke4RJaRndrE8+1z3jGSjoqPYNsNT7tYrvIrtcfsDvSl+qWSLJdI9JlHoucWzHd1jEvkKDqBssVzonpNkrmKpuK6X6B6UJFZTxQ50D0rSsJVUcX3dg5JsbVMJj9WFnO+qqXI21D0phZom2VpZ656U4LWnqspK96gEQ1VVbE5XtyPvhSBzYoo+9CkupyeIS9Eq45dXtWO6uJwuWBK7Imb8slTamTem4MN/Y6a6RyUIXUKV0qvrsWwXs6p7VIKO6JD7KqVSrz8ey2WxdI9KMCBWKTXf9G+kutR0j0oQUKuUmt03bycyXXSPSpCSq2Rnl+679/Qupu5RCdJKTcxBlWy5dN99mJiCW37nMrp1u5Wpki2XXvfjJ1oXe657VnFVuSqlZi/r8nnyglClpXtWcbJV9sule3s3Ed2+5jK6c1sVHeq3Kvvl0r29bwvuwDyNKvlyybrsnBuxKpyOoGOq5Mul1+1d10S6nE6V/XLJuzjPrYovZtp/ssr+7NLb3f95NydVJVsuu+wI+vMOTqvK1X1baAeVE6pyddcW3AOrKoJRnq7y5bPYOjmlKl8/tafCUU6kytcPlCa8qmwlq3x7T2vCq0rqO2J+qfLtbXsquN1PFUZ3EmSq5E1EN3tUY3TXKSBXedWnr5McpzewDIhVmv/INeFVpUGq0ryeSjZxHE6vB4WUKrtpW7aJ43B67TDyLTHT/q3TdgQf/ASH0+vMK9Eqln9Mk6wKp/ckLIWrHMkZ6B6VYKSsykz3qARDZVU4vQNsrqxKrHtUCquuhn+pe1KKqqIsPqt3IQeqqjB6cmgYM0VVOF3aGkZslVWwOF2uGMbGUVOF139NGVUlVRxWJ9vsWbOSQ4jXacUwFioOoTqnK9u9VEEVi9EN/gdrq1q0Mqenht8F9aKr8FsqhtEqFx0l1j2ijEW50C7crlV+aKUFHkT1WPd40pJqQV2sgOE55VE8KNfr/+uRlF2mlGdMP+rqwGadzAbBwziHhAo8XrFlG1fTYDB7Fh+jd+B83houFqP1wactznKDXPBgEOTf5D8NwyhKklUc7z928WLO6n//AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ61fwHLexJTqaJ92QAAAABJRU5ErkJggg==',
            style={
                'height': '4%',
                'width': '3%',
                'float': 'right',
                'position': 'right',
                'padding-top': 0,
                'padding-right': 0
            })
    ], href='https://www.youtube.com/channel/UCBS_Q-XwVdvWftLXRlpuu_w'),

    html.A([
        html.Img(
            src='data:image/png;base64,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',
            style={
                'height': '4%',
                'width': '3%',
                'float': 'right',
                'position': 'right',
                'padding-top': 2,
                'padding-right': 0
            })
    ], href='https://twitter.com/TraffikHub'),
html.A([
        html.Img(
            src='data:image/png;base64,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',
            style={
                'height': '1%',
                'width': '1%',
                'float': 'right',
                'position': 'right',
                'padding-top': 8,
                'padding-right': 0
            })
    ], href='https://www.linkedin.com/company/traffik-analysis-hub/?viewAsMember=true'),
    html.H1('Human Trafficking - Job Advertisement', style={'color': colors['heading'], 'textAlign': 'center'}),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='General Information', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Industry', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Country', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Locanto Link', value='tab-4', style=tab_style, selected_style=tab_selected_style),
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
                          figure=px.bar(df,x = "ad id", y="risk score", title='Risk score Bar Chart', color = 'risk score', color_continuous_scale=px.colors.sequential.Viridis))
            ], className="six columns"),

            html.Div([
                html.H5('Graph Example 2', style={'color': colors['tabBarColor'], 'textAlign': 'center'}),
                dcc.Graph(id='g2',
                          figure=px.pie(df, values='risk score', names='country', color_discrete_sequence=px.colors.sequential.Viridis)
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


        ]),

if __name__ == '__main__':
    app.run_server(debug=True)
