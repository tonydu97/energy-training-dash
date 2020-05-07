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
lst_pages = ['introduction', 'pros-cons', 'use-cases']


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
            ),href='http://www.crai.com/industry/energy'
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
                        dbc.NavLink('Introduction to Dash', href='/introduction', id='page-1-link', active=True, style={'fontSize':20}),
                        dbc.NavLink('Advantages and Disadvantages of Dash', href='/pros-cons', id='page-2-link', style={'fontSize':20}),
                        dbc.NavLink('Potential Use Cases', href='/use-cases', id='page-3-link', style={'fontSize':20}),                       
                    ],
                    vertical = True, 
                    pills = True,
                )
            ]
        )
    ]
)

CONTENT = dbc.Card(
    id='page-content'
)


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



INTRODUCTION = html.P('This is the content of page 1!')

PROS_CONS = html.P('This is the content of page 2!')

USE_CASES = html.P('This is the content of page 3!')

# Callback Functions
@app.callback(
    [Output(f'page-{i}-link', 'active') for i in range(1, 4)],
    [Input('url', 'pathname')],
)
def toggle_active_links(pathname):
    if pathname == '/':
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f'/{page}' for page in lst_pages]


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname in ['/', '/' + lst_pages[0]]:
        return INTRODUCTION
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