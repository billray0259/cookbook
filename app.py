# Import required libraries
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from globals import app
from pages import home, create_recipe


# Define the navigation menu
nav_menu = dbc.Container(
    dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("Home", href="/", className="nav-link"), className='nav-item'),
            dbc.NavItem(dbc.NavLink("Breakfast", href="/breakfast", className="nav-link"), className='nav-item'),
            dbc.NavItem(dbc.NavLink("Lunch", href="/lunch", className="nav-link"), className='nav-item'),
            dbc.NavItem(dbc.NavLink("Dinner", href="/dinner", className="nav-link"), className='nav-item'),
            dbc.NavItem(dbc.NavLink("Dessert", href="/dessert", className="nav-link"), className='nav-item'),
            dbc.NavItem(dbc.NavLink("Drinks", href="/drinks", className="nav-link"), className='nav-item'),
            dbc.NavItem(dbc.NavLink("Create Recipe", href="/create-recipe", className="nav-link"), className='nav-item'),
        ],

        pills=True,
        
    ),
    # style={
    #     # "background-color": "#f8f9fa",
    #     # "background-color": "primary",
    #     # "border-radius": "10px",
    #     "padding": "10px",
    #     "margin-top": "10px",
    #     "margin-bottom": "10px",
    # },
    className="navbar navbar-expand-lg navbar-light bg-light mb-4",
)

# Set the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav_menu,
    html.Div(id='page-content')
])

# Define the app callbacks
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/breakfast':
        return "This is the breakfast page"
    elif pathname == '/lunch':
        return "This is the lunch page"
    elif pathname == '/dinner':
        return "This is the dinner page"
    elif pathname == '/dessert':
        return "This is the dessert page"
    elif pathname == '/drinks':
        return "This is the drinks page"
    elif pathname == '/create-recipe':
        return create_recipe.layout
    else:
        return "404 Page Error"


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8000)
