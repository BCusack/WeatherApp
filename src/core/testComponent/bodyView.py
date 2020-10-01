import dash
import dash_html_components as html
import dash_bootstrap_components as dbc


body = html.Div(
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
