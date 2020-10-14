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


data = get_data()
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(
    children=[
        navView.navbar,
        html.Div(
            children=[
                dbc.Row(
                    dbc.Col(
                        html.H3(data["Station Name"][0] + " Weather Data Analysis"),
                    ),
                    className="title text-center mt-3",
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


@app.callback(
    Output("corr_graph", "figure"),
    [Input("xinput", "value"), Input("yinput", "value")],
)
def update_corr_graph(xvalue, yvalue):
    dataFrame = data
    c_fig = go.Figure()
    c_fig.add_trace(
        go.Scatter(
            y=dataFrame[xvalue],
            x=dataFrame[yvalue],
            mode="markers",
        )
    )

    c_fig.update_layout(
        height=600,
        autosize=False,
        xaxis={"title": xvalue, "type": "linear"},
        yaxis={"title": yvalue, "type": "linear"},
        margin={"l": 40, "b": 40, "t": 10, "r": 0},
        hovermode="closest",
    )
    return c_fig


@app.callback(
    Output("scatter_graph", "figure"),
    [Input("my-range-slider", "value"), Input("dropdown_filter", "value")],
)
def build_graph(years, selected):
    dataFrame = data
    dataFrame["year"] = dataFrame["Date"].dt.year
    ini = {}
    ini = dataFrame["year"].unique()
    start_date = ini[years[0]]
    end_date = ini[years[1]]
    mask = (dataFrame["year"] >= start_date) & (dataFrame["year"] <= end_date)
    dataFrame = dataFrame.loc[mask]
    fig = go.Figure()
    array_length = len(selected)
    if len(selected) > 0:
        for i in range(array_length):
            fig.add_trace(
                go.Scatter(
                    y=dataFrame[selected[i]],
                    x=dataFrame["Date"],
                    name=selected[i],
                    mode="markers",
                )
            )
    else:
        fig.add_trace(
            go.Scatter(y=dataFrame["Max_Temp"], x=dataFrame["Date"], name="Max Temp")
        )
    fig.update_layout(
        showlegend=True,
        height=600,
        autosize=False,
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
