import json
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd
from dash import Dash

colors = {
    'background': '#FFFFFF',
    'heading': '#000000',
    'light_grey': '#D3D3D3',
}

with open('dummyData.json') as json_file:
    data_two = json.load(json_file)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
app.css.append_css(
    {'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'})

job_title = [i['Job_title']['title'] for i in data_two["ads"]]
ad_id = [i['Ad_id']['id'] for i in data_two["ads"]]
country = [i['Country']['country'] for i in data_two["ads"]]
language = [i['language'] for i in data_two["ads"]]
risk_score = [i['keywords']['relevance'] for i in data_two["ads"]]
text = [i['keywords']['text'] for i in data_two["ads"]]
count = [i['keywords']['count'] for i in data_two["ads"]]
text_characters = [i['usage']['text_characters'] for i in data_two["ads"]]
df2 = pd.DataFrame(
    {'job title': job_title, 'count': count, 'ad id': ad_id, 'country': country, 'text': text, 'risk score': risk_score,
     'language': language, 'text characters': text_characters})
df2.sort_values(by=['risk score'], inplace=True)

maxRisk = df2['risk score'].nlargest(n=6)
minimum = maxRisk.min()
top_5 = df2[df2['risk score'] > minimum]

newJob_title = [i['Job_title']['title'] for i in data_two["ads"]]

my_list = [0.94, 0.98]

fig4 = px.bar(top_5, x="job title", y="risk score",range_y=my_list, color = 'risk score', color_continuous_scale=px.colors.sequential.Magma)
fig4.update_layout(paper_bgcolor='#D3D3D3')
fig4.update_layout(plot_bgcolor='#F5F5F5')
fig4.update_layout(title_text='Top 5 ads and their Job Title', title_x=0.5)

fig2 = px.bar(df2, x="text characters", y="job title", color='text characters',
              color_continuous_scale=px.colors.sequential.Magma)
fig2.update_layout(paper_bgcolor='#D3D3D3')
fig2.update_layout(plot_bgcolor='#F5F5F5')
fig2.update_layout(title_text='Amount of characters in each Ad', title_x=0.5)

fig = px.pie(df2, values='count', names='text', color_discrete_sequence = px.colors.sequential.Magma)
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.update_layout(paper_bgcolor='#D3D3D3')
fig.update_layout(plot_bgcolor='#F5F5F5')
fig.update_layout(title_text='Keyword in Advertisement', title_x=0.5)

fig3 = px.bar(df2, x="ad id", y="risk score", color='risk score', color_continuous_scale=px.colors.sequential.Magma)
fig3.update_layout(paper_bgcolor='#D3D3D3')
fig3.update_layout(plot_bgcolor='#F5F5F5')
fig3.update_layout(title_text='Risk score Bar Chart', title_x=0.5)

app.layout = html.Div(style={'backgroundColor': colors['light_grey']}, children=[

    html.Div(
        className="app-header",
        children=[
            html.A([
                html.Img(
                    src='https://cdn.pixabay.com/photo/2016/08/09/17/52/instagram-1581266_1280.jpg',
                    style={
                        'width': '2%',
                        'float': 'right',
                        'position': 'right'
                    })
            ], href='https://www.instagram.com/accounts/login/?next=/traffikanalysishub/'),
            html.A([
                html.Img(
                    src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjmQ27sh4TAODzZPZduE0rh6oScgZo2vq9XyZ2kmNfekHQI8BxvYGuB4w-rnZFkPidud0&usqp=CAU',
                    style={
                        'width': '1.5%',
                        'float': 'right',
                        'position': 'right',
                        'padding-top': 4,
                        'padding-right': 4
                    })
            ], href='https://www.linkedin.com/company/traffik-analysis-hub/?viewAsMember=true'),
            html.A([
                html.Img(
                    src='https://avaazdo.s3.amazonaws.com/original_5c1d5b2493141.jpg',
                    style={
                        'width': '2.5%',
                        'float': 'right',
                        'position': 'right',
                        'padding-top': 6,
                        'padding-right': 0
                    })
            ], href='https://www.youtube.com/channel/UCBS_Q-XwVdvWftLXRlpuu_w'),

            html.A([
                html.Img(
                    src='https://cdn.freebiesupply.com/logos/large/2x/twitter-logo-png-transparent.png',
                    style={
                        'width': '1.5%',
                        'float': 'right',
                        'position': 'right',
                        'padding-top': 7,
                        'padding-right': 0
                    })
            ], href='https://twitter.com/TraffikHub'),
            html.Div('spacing for traffic button', className="app-space--title"),
            html.Div('Analysis of Human Trafficking Evident in Job Advertisements', className="app-header--title"),
            html.Div('About Us', className="app-about--title"),
            html.Div('We are a group of students in second and third year computer science in Trinity. ',
                     className="app-description--title"),
            html.Div('We have come together with IBM to work with the Traffic Analysis Hub. ',
                     className="app-description--title"),
            html.Div('The aim of our project is to determine whether an add has signs of human trafficking.',
                     className="app-description--title"),
            html.Div('We have used a risk score to determine if there is signs of human trafficking.',
                     className="app-description--title"),
            html.Div('Click for more info:', className="app-description--title"),
            html.A([
                html.Img(
                    src='https://pbs.twimg.com/profile_images/1356645900576260096/2MfwhwLc_400x400.jpg',
                    style={
                        'width': '2%',
                        'float': 'centre',
                        'position': 'centre',
                        'padding-left' : 930
                    })
            ], href='https://www.traffikanalysis.org/'),
        ]
    ),

    html.Div([

        html.Div([
            dcc.Graph(id='g1',
                      figure=fig3
                      ),
        ], className="six columns"),
        html.Div([
            dcc.Graph(id='g2',
                      figure=fig2
                      ),
        ], className="six columns"),
    ], className="row"),

    html.Div([
        html.Div([
            dcc.Graph(
                id='graph',
                figure=fig
            ),
        ], className="six columns"),
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=fig4
            ),
        ], className="six columns"),
    ], className="row"),
])

if __name__ == '__main__':
    app.run_server(debug=True)