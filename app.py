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
lst_pages = ['intro', 'why-dash', 'analysis', 'visualization', 'demo', 'use-cases']


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # for Heroku deployment


HEADBAR = dbc.Navbar(
    children=[
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url('branding.png'), height='40px')),
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
        html.Div(
            [
                html.H3(children="Agenda", className='display-5'),
                html.Hr(className='my-2'),
                #html.Label("Today's Agenda", className='lead'),
                dbc.Nav(
                    [
                        dbc.NavLink('Introduction to Dash', href='/intro', id=lst_pages[0], style={'fontSize':20}),
                        dbc.NavLink('Why Dash', href='/why-dash', id=lst_pages[1], style={'fontSize':20}),
                        dbc.NavLink('Data Analysis with Dash', href='/analysis', id=lst_pages[2], style={'fontSize':20}),
                        dbc.NavLink('Data Visualization with Dash', href='/visualization', id=lst_pages[3], style={'fontSize':20}),
                        dbc.NavLink('Dash Application Demo', href='/demo', id=lst_pages[4], style={'fontSize':20}),
                        dbc.NavLink('Potential Use Cases', href='/use-cases', id=lst_pages[5], style={'fontSize':20}),                       
                    ],
                    vertical = True, 
                    pills = True,
                )
            ]
        )
    ], style={'height': '100%'}
)

CONTENT = html.Div(
    [
        dbc.Card(id='page-content', style={'height':'720px'})
    ]
)


BODY = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(NAV_PANE, width=3),
                dbc.Col(CONTENT),
            ],
            style={'marginTop': 30, 'marginLeft': 30, 'marginRight': 100},
        )
    ],
    className='mt-12', fluid = True
)


HOME = dbc.CardBody(
    children=[
        dbc.Row(
            [
                dbc.Col(html.Img(src=app.get_asset_url('energy.png'), height='300px'), width=4),
                dbc.Col(
                    children=[
                        html.H1('Python Web Applications in Dash'),
                        html.Img(src=app.get_asset_url('dash.png')),
                        html.H3('May 22, 2020'),       
                    ]
                ),
            ], align='center'
        ), 

    ]
)

DASH_INTRO = dbc.CardBody(
    [
        dbc.Row(html.H1('Dash is a Python library for creating web applications'),style={'marginLeft': '10px'},),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown('''
                        &nbsp;
                        * ## Front-end user interface in web browser 
                        &nbsp;
                        * ## Back-end functions in Python 
                        &nbsp;
                        * ## Ability to leverage other Python packages
                            * ### Pandas, Numpy, Plotly
                        ''')
                    ], width=7
                ),
                dbc.Col(
                    [
                        html.Img(src = app.get_asset_url('MVC.png'), height = '350px', style = {'marginTop': '10px'})
                    ], #width=6
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Alert(children=html.H3('Dash can be a powerful tool for data analysis and visualization', 
                style={'textAlign': 'Center'}), color='primary', style={'width': '100%'})
            ], style={'marginTop':'30px'}
        )
    ]
)


WHY_DASH = dbc.CardBody(
    [
        dbc.Row(html.H1('Dash combines a graphical user interface with the computational advantages of programming'),style={'marginLeft': '10px'},),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown('''
                        &nbsp;
                        * ## Reproducibility 
                        &nbsp;
                        * ## Modeling and calculation capabilities 
                        &nbsp;
                        * ## Computational efficiency 
                        &nbsp;
                        * ## Ability to work with large data sets across multiple sources 
                        ''')
                    ], width=12
                ),
                dbc.Col(
                    [
                       
                    ], 
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Alert(children=html.H3('Dash can be a powerful tool for data analysis and visualization', 
                style={'textAlign': 'Center'}), color='primary', style={'width': '100%'})
            ], style={'marginTop':'30px'}
        )
    ]
)

ANALYSIS = html.Div()

VISUALIZATION = html.Div()

DEMO = html.Div()


USE_CASES = dbc.Card(
    [
        dbc.CardBody(
            children=[
                dcc.Markdown('''
                # Dash is a Python library for creating web applications
                &nbsp;
                * ##### Front-end user interface in web browser
                &nbsp;
                * ##### Back-end functions in Python
                &nbsp;
                * ##### Python back-end to perform data processing and visualization
                ''')
            ]
        )
    ], style={'height':'720px'}
)



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
        return WHY_DASH
    elif pathname == '/' + lst_pages[2]:
        return ANALYSIS
    elif pathname == '/' + lst_pages[3]:
        return VISUALIZATION
    elif pathname == '/' + lst_pages[4]:
        return DEMO
    elif pathname == '/' + lst_pages[5]:
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