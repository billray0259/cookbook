# Import required libraries
import dash_bootstrap_components as dbc
from dash import Dash
import os

DATABASE_FILE = 'data/database.json'
IMAGE_FOLDER = 'data/images'


if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, 'w') as f:
        f.write('{}')

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)