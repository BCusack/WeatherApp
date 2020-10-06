import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app, server
from src.core.WeatherApp import layout

import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = layout
app.enable_dev_tools


@app.callback(
    Output("example-output", "children"), [Input("example-button", "n_clicks")]
)
def on_button_click(n):
    return f"Clicked {n} times."


if __name__ == "__main__":
    app.run_server(debug=True)
