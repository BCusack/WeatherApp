import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from src.dfService import get_data

df = get_data()

body = html.Div(
    children=[
        dbc.Row(html.H3("Correlation Graph Inputs"), className="pt-3"),
        dbc.Row(
            children=[
                dbc.Col(
                    dcc.Dropdown(
                        id="xinput",
                        options=[
                            {"label": label, "value": label}
                            for label in df
                            if label != "Date"
                            if label != "Pan_Evaporation"
                            if label != "Station Name"
                        ],
                        placeholder="Graph X ",
                        value="Max_Temp",
                    ),
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="yinput",
                        options=[
                            {"label": label, "value": label}
                            for label in df
                            if label != "Date"
                            if label != "Pan_Evaporation"
                            if label != "Station Name"
                        ],
                        placeholder="Graph Y ",
                        value="Evapo_Transpiration",
                    ),
                ),
            ],
            className="p-3",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [dcc.Graph(id="corr_graph")],
                    ),
                ),
            ),
        ),
    ]
)
