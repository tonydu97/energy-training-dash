'''

CRA Energy Training Presentation on Dash in Dash
Tony Du


'''


import pathlib
import os
import glob


import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import pandas as pd
import numpy as np
import json
import plotly.graph_objects as go
import plotly.express as px




# global vars
dirname = os.path.dirname(__file__)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # for Heroku deployment


HEADBAR = dbc.Navbar(
    children=[
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url('branding.png'), height='40px')),
                    dbc.Col(
                        dbc.NavbarBrand('Energy Training 5/22', className='ml-2')
                    ),
                ],
                align='center',
                no_gutters=True,
            ),href="http://www.crai.com/industry/energy"
        )
    ],
    color='dark',
    dark=True,
    sticky='top',
)

NAV_PANE = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H4(children='Python Web Apps in Dash', className='display-5'),
                html.Hr(className='my-2'),
                html.Label("Today's Agenda", className='lead'),
                dbc.Nav(
                    [
                        dbc.NavLink("Page 1", href="/page-1", id="page-1-link", active=True),
                        dbc.NavLink("Page 2", href="/page-2", id="page-2-link"),
                        dbc.NavLink("Page 3", href="/page-3", id="page-3-link"),                       
                    ],
                    vertical = True, 
                    pills = True,
                )
            ]
        )
    ]
)

CONTENT = dbc.Card()



BODY = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(NAV_PANE, md=3, align='center'),
                dbc.Col(dbc.Card(CONTENT), md=9),
            ],
            style={'marginTop': 30},
        )
    ],
    className='mt-12', fluid = True
)

app.title = 'CRA Energy Training'
app.layout = html.Div(children=[HEADBAR, BODY])
if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port='8050', debug=True, dev_tools_ui=True)