import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from src import filters, tableView, slider, correlationView

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
                                [dcc.Graph(id="scatter_graph")],
                            ),
                        ),
                        width={"size": 10, "offset": 1},
                    ),
                ),
                dbc.Row(
                    dbc.Col(slider.slider, width={"size": 10, "offset": 1}),
                ),
                dbc.Row(
                    dbc.Col(
                        correlationView.body,
                        width={"size": 10, "offset": 1},
                    ),
                    className="p-3",
                ),
                dbc.Row(
                    dbc.Col(tableView.table, width={"size": 10, "offset": 1}),
                ),
            ]
        ),
    ]
)
