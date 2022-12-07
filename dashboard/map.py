from dash import Dash, dcc, html, Input, Output, State


def map():
     map = html.Div([
            html.P("Select a crime:"),
            dcc.RadioItems(
                id='crime',
                options=['murders',
                            'rapes',
                            'robberies',
                            'assaults',
                            'burglaries', 'larcenies', 'autoTheft', 'arsons'],
                value='murders',
                inline=True
            ),
            dcc.Graph(id="graph"),
        ])

     return map