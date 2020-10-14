import dash_html_components as html
import dash
import dash_table
from src.dfService import get_data

df = get_data()

table = html.Div(
    children=[
        html.Span(id="dTable"),
        dash_table.DataTable(
            id="table",
            data=df.to_dict("records"),
            columns=[
                {"name": i, "id": i} for i in df.columns if i != "Pan_Evaporation"
            ],
            page_size=30,
            style_table={"margin-top": "30px", "textAlign": "center"},
            style_header={
                "backgroundColor": "white",
                "fontWeight": "bold",
                "textAlign": "center",
            },
            filter_action="native",
            sort_action="native",
        ),
    ],
    id="dataTable",
)
