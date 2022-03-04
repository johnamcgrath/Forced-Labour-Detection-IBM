# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

app = Dash(__name__)

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])

df_bar = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig2 = px.bar(df_bar, x="Fruit", y="Amount", color="City", barmode="group")

df = px.data.iris()  # iris is a pandas DataFrame
fig3 = px.scatter(df, x="sepal_width", y="sepal_length")

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div(children=[

    html.Div([
        html.H1(children='Sweng Project Group 23'),

        html.Div(children='''
             This is a demo of some graphs we could use.
        '''),

        html.Div(children='''
            Below is a line graph.
        '''),

        dcc.Graph(figure=fig),
    ]),

    html.Div([

        html.Div(children='''
            Below is a bar chart.
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig2
        ),
    ]),

    html.Div([

       html.Div(children='''
            Below is a scatter plot.
        '''),

        dcc.Graph(
            id='graph3',
            figure=fig3
        ),
    ]),

])


if __name__ == '__main__':
    app.run_server(debug=True)

