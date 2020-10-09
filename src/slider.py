import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from .dfService import get_data
import pandas as pd

df = get_data()
df.index = df["Date"]
df["year"] = df["Date"].dt.year
years = {}
years = df["year"].unique()

slider = html.Div(
    [
        html.Label(
            ["Date Filter"],
            style={"font-weight": "bold"},
        ),
        html.P(),
        dcc.RangeSlider(
            id="my-range-slider",
            min=0,
            max=len(years) - 1,
            step=1,
            value=[6, int((len(years) - 1))],
            allowCross=False,
            updatemode="mouseup",
            marks={i: " {}".format(years[i]) for i in range(0, len(years - 1))},
        ),
    ]
)
