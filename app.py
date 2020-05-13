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
lst_pages = ['dash-intro', 'pros-cons', 'use-cases']


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # for Heroku deployment


HEADBAR = dbc.Navbar(
    children=[
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url('branding.png'), height='50px')),
                    dbc.Col(
                        dbc.NavbarBrand('Energy Training', className='ml-2')
                    ),
                ],
                align='center',
                no_gutters=True,
            ),href='/'
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
                html.H4(children="Today's Agenda", className='display-5'),
                html.Hr(className='my-2'),
                #html.Label("Today's Agenda", className='lead'),
                dbc.Nav(
                    [
                        dbc.NavLink('Introduction to Dash', href='/dash-intro', id=lst_pages[0], style={'fontSize':20}),
                        dbc.NavLink('Advantages and Disadvantages of Dash', href='/pros-cons', id=lst_pages[1], style={'fontSize':20}),
                        dbc.NavLink('Potential Use Cases', href='/use-cases', id=lst_pages[2], style={'fontSize':20}),                       
                    ],
                    vertical = True, 
                    pills = True,
                )
            ]
        )
    ], style={'height':'100%'}
)

CONTENT = html.Div(
    id='page-content'
)


BODY = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(NAV_PANE, md=3),
                dbc.Col(dbc.Card(CONTENT)),
            ],
            style={'marginTop': 30, 'marginLeft': 100, 'marginRight': 100},
        )
    ],
    className='mt-12', fluid = True
)


HOME = dbc.Card(
    dbc.CardBody(
        children=[
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url('energy.png'), height='300px'), md=4),
                    dbc.Col(
                        children=[
                            html.H1('Python Web Applications in Dash'),
                            html.Img(src=app.get_asset_url('dash.png')),
                            html.H3('May 22, 2020'),       
                        ], md=8
                    ),
                ], align='center'
            ), 

        ]
    ), #className='vh-100', 
    style={'height':'720px'}

)

DASH_INTRO = dbc.Card(
    [
        dbc.CardHeader(html.H3('What is Dash?')),
        dbc.CardBody(
            children=[
                dcc.Markdown('''
                # Dash is a Python library for creating web applications
                &nbsp;
                * ##### Web application front-end user interface
                &nbsp;
                * ##### Python back-end to perform data processing and visualization
                ''')
            ]
        )
    ]
)

PROS_CONS = html.P('This is the content of page 2!')

USE_CASES = html.P('This is the content of page 3!')

# Callback Functions
@app.callback(
    [Output(f'{page}', 'active') for page in lst_pages],
    [Input('url', 'pathname')],
)
def toggle_active_links(pathname):
    return [pathname == f'/{page}' for page in lst_pages]


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname in ['/', '/home']:
        return HOME
    elif pathname == '/' + lst_pages[0]:
        return DASH_INTRO
    elif pathname == '/' + lst_pages[1]:
        return PROS_CONS
    elif pathname == '/' + lst_pages[2]:
        return USE_CASES
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1('404: Not found', className='text-danger'),
            html.Hr(),
            html.P(f'The pathname {pathname} is invalid'),
        ]
    )



app.title = 'CRA Energy Training'
app.layout = html.Div(children=[dcc.Location(id='url'), HEADBAR, BODY])
if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port='8050', debug=True, dev_tools_ui=True)