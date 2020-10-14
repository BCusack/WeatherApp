import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from src.dfService import get_data

df = get_data()

filters = html.Div(
    dcc.Dropdown(
        id="dropdown_filter",
        options=[
            {"label": label, "value": label}
            for label in df
            if label != "Date"
            if label != "Pan_Evaporation"
        ],
        placeholder="Grah Display",
        value=["Max_Temp"],
        multi=True,
    ),
    className="p-3",
)
