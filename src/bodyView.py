import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from src.slider import slider
from src import filters
from dash.dependencies import Input, Output
from app import app

body = html.Div(
    [
        html.Div(
            children=[
                dbc.Row(
                    dbc.Col(filters.filters, width={"size": 10, "offset": 1}),
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    dcc.Graph(
                                        id="scatter_graph",
                                    )
                                ],
                                style={"heigth": "70vh"},
                            ),
                        ),
                        width={"size": 10, "offset": 1},
                    ),
                ),
                dbc.Row(
                    dbc.Col(slider, width={"size": 10, "offset": 1}),
                ),
            ]
        ),
    ]
)
