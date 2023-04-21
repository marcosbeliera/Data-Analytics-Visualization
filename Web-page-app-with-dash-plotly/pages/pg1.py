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
                   path='/', # '/' is home page and it represents the url
                   name='Diversity by Ethnicities', # name of page, commonly used as name of link
                   title='uspopulation', # title that appears on browser's tab
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

# -------------- Plot 1 = Horizontal barplot US Population 2020 versus US Hair Companies 2021/22 ------------------------------------

# Data Treatement
df_us_census_eth_plt = df_us_census_eth.copy()
df_us_census_eth_plt['tag_name'] = df_us_census_eth_plt.tag_name.str.upper()
df_us_census_eth_plt = df_us_census_eth.copy().T
df_us_census_eth_plt.columns = list(df_us_census_eth_plt.iloc[0,:])
df_us_census_eth_plt = df_us_census_eth_plt.drop(df_us_census_eth_plt.index[0])
df_us_census_eth_plt.columns = df_us_census_eth_plt.columns.str.upper()

df = df_us_census_eth_plt.copy()
df = df.rename(index = {'population_percentage' : 'US Hair Companies 2021/22', 'ethnicity_percentage': 'US Population 2020'})

fig1 = go.Figure()

fig1.add_trace(go.Bar(
    y=df.index,
    x=df.iloc[:,0],
    name=df.columns[0],
    orientation='h',
    text = df.iloc[:,0].apply(lambda x: f"{x:.0f}%"),
    textposition = 'inside'
))
fig1.add_trace(go.Bar(
    y=df.index,
    x=df.iloc[:,1],
    name=df.columns[1],
    orientation='h',
    text = df.iloc[:,1].apply(lambda x: f"{x:.0f}%"),
    textposition = 'inside'
))

fig1.add_trace(go.Bar(
    y=df.index,
    x=df.iloc[:,2],
    name=df.columns[2],
    orientation='h',
    text = df.iloc[:,2].apply(lambda x: f"{x:.0f}%"),
    textposition = 'inside'
))

fig1.add_trace(go.Bar(
    y=df.index,
    x=df.iloc[:,3],
    name=df.columns[3],
    orientation='h',
    text = df.iloc[:,3].apply(lambda x: f"{x:.0f}%"),
    textposition = 'inside'
))

fig1.add_trace(go.Bar(
    y=df.index,
    x=df.iloc[:,4],
    name=df.columns[4],
    orientation='h',
    text = df.iloc[:,4].apply(lambda x: f"{x:.0f}%"),
    textposition = 'inside'
))

fig1.add_trace(go.Bar(
    y=df.index,
    x=df.iloc[:,5],
    name=df.columns[5],
    orientation='h',
    text = df.iloc[:,5].apply(lambda x: f"{x:.0f}%"),
    textposition = 'inside'
))

fig1.update_layout( 
                    barmode = 'stack',
                    autosize = True,
                    plot_bgcolor='WHITE',
                    legend=dict(font = dict(size = 18),
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

# -------------- Plot 2 = Horizontal barplot AGE US Diversity index calculation by Top HairCare Companies ------------------------------------

# Multi-categorical Axes
alphabet = list(string.ascii_lowercase)
alphabet = [x.upper() for x in alphabet]

# Anonimizo nombres de brands
all_brand_list = df_list_entropy_eth.brand_name.unique()
diccionario = {}
for i in reversed(range(len(df_list_entropy_eth))):
    diccionario[all_brand_list[i]] = "Company "+alphabet[len(df_list_entropy_eth) - i - 1 ]

brand_name_unnamed_2 = df_list_entropy_eth.brand_name.replace(diccionario) 


fig2 = make_subplots(rows=1, cols = 2,specs = [[{}, {}]],
                    horizontal_spacing = 0.2,
                    shared_xaxes=False,
                    subplot_titles=['Diversity Index (%)','Sample of Assets by Company']
)

fig2.add_trace(go.Bar( x = df_list_entropy_eth['entropy_21'],
                      y = brand_name_unnamed_2,
                      name = "2021",
                      legendgroup="2021",
                      marker_color='blue',
                      orientation = 'h',
                      text = df_list_entropy_eth['entropy_21'].apply(lambda x: f"{x}%"),
                      marker={"opacity": 0.8},
              ),
              row = 1, col = 1
)

fig2.add_trace(go.Bar(
                      x = df_list_entropy_eth['entropy_22'],
                      y = brand_name_unnamed_2,
                      name = "2022",
                      legendgroup="2022",
                      marker_color='red',
                      orientation = 'h',
                      text = df_list_entropy_eth['entropy_22'].apply(lambda x: f"{x}%"),
                      marker={"opacity": 0.8}
              ),
              row = 1, col = 1
)

fig2.add_trace(go.Bar( x = df_list_entropy_eth['asset_id_21'],
                      y = brand_name_unnamed_2,
                      name = "2021",
                      legendgroup="2021",
                      marker_color='blue',
                      orientation = 'h',
                      text = df_list_entropy_eth['asset_id_21'],
                      marker={"opacity": 0.8},
                      showlegend=False
              ),
              row = 1, col = 2
)

fig2.add_trace(go.Bar( x = df_list_entropy_eth['asset_id_22'],
                      y = brand_name_unnamed_2,
                      name = "2022",
                      legendgroup="2022",
                      marker_color='red',
                      orientation = 'h',
                      text = df_list_entropy_eth['asset_id_22'],
                      marker={"opacity": 0.8},
                      showlegend=False
              ),
              row = 1, col = 2
)

fig2.update_layout(
                    autosize = False,
                    height = 800,
                    width = 1100,
                    legend = dict(font = dict(size = 15)),
                    legend_traceorder="reversed",
                    font=dict(size=15),
                    plot_bgcolor = 'white'
)
fig2.update_traces(overwrite=True, textposition = 'outside',textfont_size=12)
fig2.update_annotations(font_size=18)
fig2.update_xaxes(visible = False)
fig2['layout']['xaxis1'].update(title='', range=[0, 100])
fig2['layout']['xaxis2'].update(title='', range=[0, 150])

# -------------- Plot 3 = From 2021 to 2022: What's Changed in terms of Diversity ------------------------------------

mean_eth_21 = np.mean(df_list_entropy_eth.entropy_21)
mean_eth_22 = np.mean(df_list_entropy_eth.entropy_22)

mean_age_21 = np.mean(df_list_entropy_age.entropy_21)
mean_age_22 = np.mean(df_list_entropy_age.entropy_22)

fig3 = go.Figure()

fig3.add_trace(go.Indicator(
                            value = mean_eth_22,
                            number = {"suffix": "%"},
                            delta = {'reference': 160},
                            gauge = {'axis': {'visible': False}},
                            domain = {'row': 0, 'column': 0},
                            mode = "number",
                            title = {'text' : 'Ethnic Diversity Mean 2022'}))

fig3.add_trace(go.Indicator(
                            value = mean_eth_21,
                            number = {"suffix": "%"},
                            delta = {'reference': 160},
                            gauge = {'axis': {'visible': False}},
                            domain = {'row': 1, 'column': 0},
                            mode = "number",
                            title = {'text' : 'Ethnic Diversity Mean 2021'}))

fig3.add_trace(go.Indicator(
                            mode = "delta",
                            value = mean_eth_22,
                            number = {'suffix': "%"},
                            delta = {'position': "top", 'reference': mean_eth_21},
                            domain = {'x': [0.5, 1], 'y': [0, 1]},
                            title = {'text' : 'Ethnic Diversity Mean in 2022 has increased'}
            )
)

fig3.update_layout(grid = {'rows': 2, 'columns': 2, 'pattern': "independent"}, width = 900, height = 500)


# description
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

                                                         * Upon analyzing the demographics of the US population, it was observed that the representation of **Black models** in hair care video campaigns of the top 20 US companies was only **6%**, which is **lower than** their representation in the general population, which stands at **12%**. This underrepresentation raises could concerns about equity and inclusion in the industry.
                                                         
                                                         * On the other hand, we observed that **Asian groups** seem to be **overrepresented** when compared the frequency of appearances in social media videos (**16%**) versus the overall population sample (**6%**)
                                                         
                                                         * In the year 2022, there was an increase in the portrayal of different ethnic groups in advertisements, resulting in a diversity score of **73.2%**, a modest increase of **4.4** percentage points.

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
        dcc.Markdown('''### Black and Latino populations are underrepresented in hair care ads in US TikTok video campaigns''',
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

        html.Br(),
        dcc.Markdown('''### Diversity index calculation by Top HairCare Companies''',
                     style={'textAlign':'left',
                            'font-family': 'Altform regular, sans-serif'}
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(id='age-fig2',
                                  figure=fig2)
                    ],
                    width=15,
                    align='center'
                )  # center the content vertically
            ],
            justify='center'  # center the row horizontally
        ),

        dcc.Markdown('''### From 2021 to 2022: What's Changed in terms of Diversity?''',
                     style={'textAlign':'left',
                            'font-family': 'Altform regular, sans-serif'}
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(id='eth-fig3',
                                  figure=fig3)
                    ],
                    width=12,
                    align='center'
                )
            ],
            justify='center'  # center the row horizontally
        ),
    ]
)
