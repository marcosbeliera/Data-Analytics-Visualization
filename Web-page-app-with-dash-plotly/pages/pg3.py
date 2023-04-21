import dash
from dash import dcc, html, callback, Output, Input, Dash
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from plotly.graph_objs import *
from plotly.subplots import make_subplots
# data manipulation
import numpy as np
import pandas as pd
import os

# DATA IMPORT
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

unique_assets_per_brand   = pd.read_csv(location + '/data/unique_assets_per_brand.csv')

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/methodology',  # represents the url text
                   name='Methodology',  # name of page, commonly used as name of link
                   title='methodology'  # represents the title of browser's tab
)

# -------------- Plot 1 = Ads amount for the Study ------------------------------------

# Multi-categorical Axes
import string
alphabet = list(string.ascii_lowercase)
alphabet = [x.upper() for x in alphabet]

diccionario = {}
for i in reversed(range(len(unique_assets_per_brand))):
    diccionario[unique_assets_per_brand.brand_name[i]] = "Company "+alphabet[len(unique_assets_per_brand) - i - 1]

unique_assets_per_brand.brand_name = unique_assets_per_brand.brand_name.replace(diccionario)

fig1 = go.Figure()

fig1.add_trace(go.Bar(
                        x = unique_assets_per_brand.number_of_assets_21,
                        y = unique_assets_per_brand.brand_name,
                        name = "2021",
                        orientation = 'h',
                        text = unique_assets_per_brand['number_of_assets_21'],
                        marker={"opacity": 0.8}
                )
)

fig1.add_trace(go.Bar(
                        x = unique_assets_per_brand.number_of_assets_22,
                        y = unique_assets_per_brand.brand_name,
                        name = "2022",
                        orientation = 'h',
                        text = unique_assets_per_brand['number_of_assets_22'],
                        marker={"opacity": 0.8}
                )
)

fig1.update_layout(
                    title_font_size = 20,
                    autosize = False,
                    width = 1000,
                    height = 800,
                    legend = dict(font = dict(size = 20)),
                    legend_traceorder="reversed",
                    plot_bgcolor='white'
)
fig1.update_traces(overwrite=True, textposition = 'outside')
fig1.update_yaxes(tickfont=dict(size=15))

# ------------------------------------------- Description ----------------------------------

description = dbc.Col(
    [
        dbc.Card(
            id="description-card",
            children=[
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                         dcc.Markdown('''

                                                        To conduct our analysis, we collected 2718 TikTok public videos published by US HairCare companies 
                                                        in the years 2021 and 2022. We then utilized our proprietary **Memorable, Inc. 
                                                        tagging system** to scan the videos and generate associated tags with an **85% confidence interval**.

                                                        The tags associated with models featured in the advertisement were then categorized in terms of 
                                                        ethnic backgrounds and age groups. The purpose of this categorization was to compare the resulting groups 
                                                        against several sources, including the most recent US population [census data from 2020](https://www.census.gov/programs-surveys/decennial-census/decade/2020/2020-census-main.html)
                                                        , a study of the [US Population by Race](https://www.visualcapitalist.com/visualizing-u-s-population-by-race/),
                                                        and information on [TikTok users by age range in 2023](https://explodingtopics.com/blog/tiktok-demographics). 
                                                        This comparison was intended to observe which advertising campaigns vary from 
                                                        the country's population and the current users of TikTok.

                                                        Finally, our team calculated the **percentage of diversity (%)** by using the concept of 
                                                        "Entropy" to quantify the level of diversity in a given dataset for each brand. Entropy 
                                                        is calculated by the overall frequency distribution of ethnicity tags for each company during a certain 
                                                        period. For example, if a dataset contains equal numbers of two different classes (f.i. latinos and black group),
                                                        the entropy would be high. On the other hand, if a dataset contains only one class (only latinos), the entropy 
                                                        would be low because we don’t have the distribution homogeneity.

                                                        In the left picture you can observe a high entropy, while the right picture displays a lower entropy.

                                                     ''',
                                                     style={'textAlign':'left',
                                                            'fontSize': 20,
                                                            'font-family': 'Altform regular, sans-serif'}
                                         ),
                                    md=True,
                                ),
                                html.Div([
                                            html.Div([
                                                        html.Img(src='assets/img2.png', style={'width':'97%','height':'97%'})
                                                    ],
                                                        className='column',style={"display": "inline-block"}),
                                            html.Div([
                                                        html.Img(src='assets/img1.png', style={'width':'97%','height':'97%'})
                                                    ],
                                                        className='column', style={"display": "inline-block"})
                                        ],
                                        className='column',
                                        style={"display": "flex", "flexDirection": "row"}
                                    ),
                                dbc.Col(
                                         dcc.Markdown(  '''
                                                        In order to access the raw data, kindly contact the Services Memorable Department for further information.
                                                        ''',
                                                     style={'textAlign':'left',
                                                            'fontSize': 20,
                                                            'font-family': 'Altform regular, sans-serif'}
                                         ),
                                    md=True,
                                ),
                            ]
                        ),
                    ]
                ),
            ],
        )
    ],
    md=12,
)

# -------------- Layouts ------------------------------------

layout = html.Div(
    [
        html.Br(),
        dcc.Markdown(f'### Data Collection and Analysis Techniques'),

        html.Br(),
        dbc.Row(description),
        
        html.Br(),
        dcc.Markdown(f'### What is the composition of the dataset used for the analysis?'),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(  id='amount_of_assets',
                                    figure=fig1)
                    ],
                    )       
            ]
        ),   
    ]
)