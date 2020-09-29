# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import csv
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


# %%
# Read data from csv into Pandas Dataframe
df = pd.read_csv("out.csv")


# %%
# Check data has been loaded into Dataframe
# df.head()


# %%
app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div(
    [
        html.Div(
            children=[
                dbc.Row(
                    dbc.Col(
                        html.H3("Weather Data Analysis"),
                    ),
                    className="text-center mt-3",
                ),
            ]
        ),
        html.Div(
            children=[
                dbc.Button("Click me", id="example-button", className="m-5"),
                html.Span(id="example-output"),
            ]
        ),
        dbc.Button("Primary", color="primary", className="mr-1"),
        dbc.Button("Secondary", color="secondary", className="mr-1"),
        dbc.Button("Success", color="success", className="mr-1"),
        dbc.Button("Warning", color="warning", className="mr-1"),
        dbc.Button("Danger", color="danger", className="mr-1"),
        dbc.Button("Info", color="info", className="mr-1"),
        dbc.Button("Light", color="light", className="mr-1"),
        dbc.Button("Dark", color="dark", className="mr-1"),
        dbc.Button("Link", color="link"),
    ]
)


@app.callback(
    Output("example-output", "children"), [Input("example-button", "n_clicks")]
)
def on_button_click(n):
    if n is None:
        return "Not clicked."
    else:
        return f"Clicked {n} times."


# %%
if __name__ == "__main__":
    app.run_server()


# %%
