import dash_bootstrap_components as dbc
import dash_html_components as html

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Data Table", href="#")),
    ],
    brand="Weather App",
    brand_href="#",
    color="primary",
    dark=True,
)
