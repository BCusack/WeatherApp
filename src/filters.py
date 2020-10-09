import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app


filters = html.Div(
    [
        dbc.Button("Evapo Transpiration", id="button1", size="sm", className="m-2"),
        dbc.Button("Rain", id="button2", size="sm", className="m-2"),
        dbc.Button("Max Temp", id="button3", size="sm", className="m-2"),
        dbc.Button("Min Temp", id="button4", size="sm", className="m-2"),
        dbc.Button("Max Humidity", id="button5", size="sm", className="m-2"),
        dbc.Button("Average Wind Speed", id="button6", size="sm", className="m-2"),
        dbc.Button("Solar Radiation", id="button7", size="sm", className="m-2"),
    ]
)


@app.callback(Output("button1", "text"), [Input("button1", "value")])
def fill_buttons(data):
    defi = "cats"
    return defi