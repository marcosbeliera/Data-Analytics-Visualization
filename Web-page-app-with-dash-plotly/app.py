import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import flask

server = flask.Flask(__name__)  # define flask
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[
                dbc.themes.SPACELAB], server=server)

sidebar = html.Div(
    [
        html.Div(
            [
                html.H2("Index", style={"color": "black",
                        'fontSize': 25, 'padding-top': '25px'}),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [dbc.NavLink([
                html.Div(page["name"], className="ms-2"),
            ],
                href=page["path"],
                active="exact",
            )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    ]
)

# header
header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.A([
                            html.Img(
                                id="logo",
                                src=app.get_asset_url(
                                    "memorable_black.png"),
                                style={'height': '20px'},
                            )
                        ], href='https://www.memorable.io/'),
                        md="auto",
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.H3("US HairCare Companies on TikTok platform", style={
                                        "color": "black", 'font-family': 'Altform regular, sans-serif', 'font-size': 30}),
                                    html.P('Diversity research', style={
                                        "color": "black", 'font-family': 'Altform regular, sans-serif'}),
                                ],
                                id="app-title"
                            )
                        ],
                        md=True,
                        align="right",
                    ),
                ],
                align="center",  # logo centrado sobre eje y
            ),
        ],
        fluid=True,
    ),
    dark=True,
    # set the background memorable color
    style={'background-color': '#B746C8'},
    # sticky="top", # fijo el header arriba
)

# layout
app.layout = dbc.Container(
    [
        header,
        dbc.Row([
            dbc.Col([sidebar],
                    xs=4, sm=5, md=4, lg=2, xl=2, xxl=2
                    ),
            dbc.Col([dash.page_container],
                    xs=8, sm=7, md=8, lg=10, xl=10, xxl=10
                    )
        ], className="g-2",
        )
    ], fluid=True
)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050, debug=True, use_reloader=True)
