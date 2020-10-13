import dash_bootstrap_components as dbc
import dash_html_components as html


filters = dbc.ButtonGroup(
    [
        dbc.Button(
            "Evapo Transpiration",
            id="button1",
            size="sm",
            outline=True,
            className=" m-2",
            color="primary",
            n_clicks=0,
        ),
        dbc.Button(
            "Rain",
            id="button2",
            size="sm",
            outline=False,
            className=" m-2",
            color="primary",
            n_clicks=0,
        ),
        dbc.Button(
            "Max Temp",
            id="button3",
            size="sm",
            outline=False,
            className=" m-2",
            color="primary",
            n_clicks=0,
        ),
        dbc.Button(
            "Min Temp",
            id="button4",
            size="sm",
            outline=False,
            className=" m-2",
            color="primary",
            n_clicks=0,
        ),
        dbc.Button(
            "Max Humidity",
            id="button5",
            size="sm",
            outline=False,
            className=" m-2",
            color="primary",
            n_clicks=0,
        ),
        dbc.Button(
            "Average Wind Speed",
            id="button6",
            size="sm",
            outline=False,
            className=" m-2",
            color="primary",
            n_clicks=0,
        ),
        dbc.Button(
            "Solar Radiation",
            id="button7",
            size="sm",
            outline=False,
            className=" m-2",
            color="primary",
            n_clicks=0,
        ),
        html.Span(id="divi1"),
    ],
    vertical=False,
    id="button_group",
)
