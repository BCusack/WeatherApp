# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

from .shared.navbar.navView import navbar
from .testComponent.bodyView import body


layout = html.Div([navbar, dbc.Container(children=[body])])
