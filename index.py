import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from app import server
from src import navView, bodyView
from src.dfService import get_data
import dash
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import datetime
import plotly.express as px

data = get_data()
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])


app.layout = html.Div(
    children=[
        navView.navbar,
        html.Div(
            children=[
                dbc.Row(
                    dbc.Col(
                        html.H3(data["Station Name"][0] + " Weather Data Analysis"),
                    ),
                    className="title text-light text-center mt-3",
                ),
                dbc.Row(
                    dbc.Col(
                        bodyView.body,
                    ),
                ),
            ]
        ),
    ]
)


@app.callback(Output("scatter_graph", "figure"), [Input("my-range-slider", "value")])
def build_graph(years):
    dataFrame = data
    dataFrame["year"] = dataFrame["Date"].dt.year
    ini = {}
    ini = dataFrame["year"].unique()
    start_date = ini[years[0] - 1]
    end_date = ini[years[1]]
    mask = (dataFrame["year"] > start_date) & (dataFrame["year"] <= end_date)
    dataFrame = dataFrame.loc[mask]
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=dataFrame["Max_Temp"], x=dataFrame["Date"], name="Max"))
    fig.add_trace(go.Scatter(y=dataFrame["Min_Temp"], x=dataFrame["Date"], name="Min"))
    fig.update_layout(showlegend=True)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
