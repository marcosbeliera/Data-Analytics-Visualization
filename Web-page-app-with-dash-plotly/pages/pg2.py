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
import string

dash.register_page(__name__,
                   path='/ageranges', # '/' is home page and it represents the url
                   name='Diversity by Ages Ranges', # name of page, commonly used as name of link
                   title='usages', # title that appears on browser's tab
                   image='pg3.png', # image in the assets folder
                   description='Learn all about the heatmap.'
)

# Import dataframes
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
df_list_entropy_eth       = pd.read_csv(location + '/data/df_list_entropy_eth.csv')
df_us_census_age          = pd.read_csv(location + '/data/df_us_census_age.csv')
df_us_census_eth          = pd.read_csv(location + '/data/df_us_census_eth.csv')
df_ethnicities_2021       = pd.read_csv(location + '/data/df_ethnicities_2021.csv')
df_ethnicities_2022       = pd.read_csv(location + '/data/df_ethnicities_2022.csv')
df_list_entropy_age       = pd.read_csv(location + '/data/df_list_entropy_age.csv')

# -------------- Plot 1 = ETH US Companies versus US Population 2021-2022 ------------------------------------

df_us_census_age_plt = df_us_census_age.copy().T
df_us_census_age_plt.columns = list(df_us_census_age_plt.iloc[0,:])
df_us_census_age_plt = df_us_census_age_plt.drop(df_us_census_age_plt.index[0:2])

df = df_us_census_age_plt.copy()
df = df.reindex(['population_tiktok','population_percentage','age_percentage'])
df = df.rename(index = {'population_tiktok' : 'TikTok Audience' , 'population_percentage': 'US Hair Companies 2021/22'})
df = df.iloc[[0,2],:]
# Plot

fig1 = go.Figure()

fig1.add_trace(go.Bar(
    x = df['Gen Z (10-25)'],
    y=['TikTok Audience' , 'US Hair Companies 2021/22'],
    name='Gen Z (10-25)',
    orientation='h',
    text = df['Gen Z (10-25)'].apply(lambda x: f"{x:.0f}%"),
    textposition = 'inside',
))
fig1.add_trace(go.Bar(
    y=['TikTok Audience' , 'US Hair Companies 2021/22'],
    x=df['Millennial (25-34)'],
    name='Millennial (25-34)',
    orientation='h',
    text = df['Millennial (25-34)'].apply(lambda x: f"{x:.0f}%"),
    textposition = 'inside'
))

fig1.add_trace(go.Bar(
    y=['TikTok Audience' , 'US Hair Companies 2021/22'],
    x=df['35-54'],
    name='p (35-54)',
    orientation='h',
    text = df['35-54'].apply(lambda x: f"{x:.0f}%"),
    textposition = 'inside'
))

fig1.add_trace(go.Bar(
    y=['TikTok Audience' , 'US Hair Companies 2021/22'],
    x=df['55+'],
    name='p (55+)',
    orientation='h',
    text = df['55+'].apply(lambda x: f"{x:.0f}%"),
    textposition = 'inside'
))

fig1.update_layout(barmode = 'stack',
                  autosize = True,
                  plot_bgcolor='white',
                  legend = dict(font = dict(size = 18),
                                yanchor="top",
                                y=0,
                                xanchor="center",
                                x=0.5,
                                orientation="h",
                                traceorder= 'normal'
                    )
)
fig1.update_yaxes(tickfont=dict(size=18))
fig1.update_xaxes(showticklabels=False)
fig1.update_traces(overwrite=True, textposition = 'inside',textfont_size=16)

# -------------- Plot 2 = AGE US Companies versus US Population 2021-2022 ------------------------------------

mean_age_21 = np.mean(df_list_entropy_age.entropy_21)
mean_age_22 = np.mean(df_list_entropy_age.entropy_22)

fig2 = go.Figure()

fig2.add_trace(go.Indicator(
    value = mean_age_22,
    number = {"suffix": "%"},
    delta = {'reference': 160},
    gauge = {'axis': {'visible': False}},
    domain = {'row': 0, 'column': 0},
    mode = "number",
    title = {'text' : 'Age Diversity Mean 2022'}))

fig2.add_trace(go.Indicator(
    value = mean_age_21,
    number = {"suffix": "%"},
    delta = {'reference': 160},
    gauge = {'axis': {'visible': False}},
    domain = {'row': 1, 'column': 0},
    mode = "number",
    title = {'text' : 'Age Diversity Mean 2021'}))

fig2.add_trace(go.Indicator(
                            mode = "delta",
                            value = mean_age_22,
                            number = {'suffix': "%"},
                            delta = {'position': "top", 'reference': mean_age_21},
                            domain = {'x': [0.5, 1], 'y': [0, 1]},
                            title = {'text' : 'Age Diversity Mean in 2022 has decresed'}
            )
)

fig2.update_layout(grid = {'rows': 2, 'columns': 2, 'pattern': "independent"}, width = 900, height = 500)

# ------------------------------------ Insights ------------------------------------------------------------------------
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

                                                      * Over 90% of TikTok hair care campaigns featured Gen Z and Millennial models, aligned with the primary audiences on the platform. However, 41% of TikTok average users are above 35+ years old, thus hinting to a missed opportunity of achieving extra reach through older audiences who also have a growing presence on the platform
                                                      
                                                      * Additionally, when analyzing age diversity across various age groups, a minor increase of only 0.4 percentage points was observed between 2021 and 2022

                                                      * However, there was a slightly higher representation (0.74 pp) of individuals aged between 35 and 54 y/o in hair care advertisements in 2022

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

# -------------- LAYOUTS ----------------------------------------------------------

layout = html.Div(
    [   html.Br(),
        dcc.Markdown('''### TikTok hair care US campaigns tend to primarily target audiences under 35 y/o missing out on extra reach''',
                     style={'textAlign':'left',
                            'font-family': 'Altform regular, sans-serif'}
        ),
        html.Br(),

        dbc.Row(description),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(id='eth-fig1',
                                  figure=fig1)
                    ],
                )
            ]
        ),

        dcc.Markdown('''### From 2021 to 2022: What's Changed in terms of Diversity?''',
                     style={'textAlign':'left',
                            'font-family': 'Altform regular, sans-serif'}
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(id='age-fig2',
                                  figure=fig2)
                    ], width=12)
            ]
        ),
    ]
)
