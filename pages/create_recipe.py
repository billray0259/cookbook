import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, ALL
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

from globals import app, DATABASE_FILE, IMAGE_FOLDER
import json
import os
import base64

def main_image_upload(image=None):
    return html.Div([
        dcc.Upload(
            id='main-image-upload',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Image')
            ]),
            className='image-upload',
            style={
                'height': '400px',
                'lineHeight': '400px',
            },
        ),
        html.Div(id='main-image'),
    ])


def ingredient_input(food=None, quantity=None, units=None, index=0):
    # first row: inline text input for food, inline float input for quantity, inline dropdown for units
    row1 = dbc.Row(
        [
            dbc.Col(
                dbc.Input(
                    type='text',
                    id={'type': 'ingredient-name-input', 'index': index},
                    placeholder='Enter ingredient name',
                    value=food,
                )
            ),
            dbc.Col(
                dbc.Input(
                    type='text',
                    id={'type': 'ingredient-quantity-input', 'index': index},
                    placeholder='Enter quantity',
                    value=quantity,
                )
            ),
            dbc.Col(
                # this should be a dropdown with the units (Cups, 1/2 Cup, 1/3 Cup, 1/4 Cup, 1/8 Cup, Tablespoon, Teaspoon, 1/2 Teaspoon, 1/4 Teaspoon)
                dcc.Dropdown(
                    id={'type': 'ingredient-unit-input', 'index': index},
                    options=[
                        {'label': 'Cups', 'value': 'Cups'},
                        {'label': '1/2 Cup', 'value': '1/2 Cup'},
                        {'label': '1/3 Cup', 'value': '1/3 Cup'},
                        {'label': '1/4 Cup', 'value': '1/4 Cup'},
                        {'label': '1/8 Cup', 'value': '1/8 Cup'},
                        {'label': 'Tablespoon', 'value': 'Tablespoon'},
                        {'label': 'Teaspoon', 'value': 'Teaspoon'},
                        {'label': '1/2 Teaspoon', 'value': '1/2 Teaspoon'},
                        {'label': '1/4 Teaspoon', 'value': '1/4 Teaspoon'},
                    ],
                    placeholder='Select unit (optional)',
                    value=units,
                ),
            ),
        ]
    )

    # second row: button to remove ingredient
    row2 = dbc.Row(
        dbc.Col(
            dbc.Button('Remove', id={'type': 'remove-ingredient-button', 'index': index}, color='danger'),
            className='mt-1',
        )
    )

    return html.Div(
        [
            row1, 
            row2
        ], 
        id={'type': 'ingredient', 'index': index},
        className='mb-2 bg-light p-2'
    )



def instruction_input(instruction=None, image=None, index=0):

    # first row: text input for step
    row1 = dbc.Row([
        dbc.Col(
            dcc.Textarea(
                id={'type': 'step-input', 'index': index},
                placeholder='Enter step',
                className='form-control',
                value=instruction,
            )
        ),
        dbc.Col([
            dcc.Upload(
                id={'type': 'step-image-upload', 'index': index},
                children=html.Div([
                    html.A('Add Image (optional)')
                ]),
                className='image-upload',
                multiple=True
            ),
            html.Div(id='output-data-upload'),
        ], width=3)
    ])

    # make buttons a button group
    row2 = dbc.Row(
        dbc.Col(
            dbc.ButtonGroup(
                [
                    dbc.Button('Remove', id={'type': 'remove-step-button', 'index': index}, color='danger'),
                    dbc.Button('Move up', id={'type': 'move-step-up-button', 'index': index}, color='primary'),
                    dbc.Button('Move down', id={'type': 'move-step-down-button', 'index': index}, color='primary'),
                ]
            ),
            className='mt-1',
        )
    )

    return html.Div(
        [
            row1, 
            row2
        ], 
        id={'type': 'step', 'index': index},
        className='mb-2 bg-light p-2'
    )


def update_index(component, new_index):
    print(component)
    # Get the properties of the original component
    props = component['props']

    # Create a new ID for the component based on the new index
    new_id = {key: new_index if key == 'index' else props['id'][key] for key in props['id']}

    # Create a new set of children with updated indices
    new_children = []
    for child in props['children']:
        if 'index' in child.props['id']:
            new_child_index = int(child.props['id']['index']) + new_index - int(props['id']['index'])
            new_child = update_index(child, new_child_index)
        else:
            new_child = child
        new_children.append(new_child)

    # Create the new component with updated properties and children
    new_component = component.type(
        id=new_id,
        className=props['className'],
        style=props['style'],
        children=new_children,
        **props['kwargs']
    )

    return new_component






def create_food_form(main_image=None, category=None, food_name=None, servings=None, time=None, ingredients=None, instructions=None):

    ingredient_components = []
    if ingredients is None:
        ingredients = [{'food': None, 'quantity': None, 'units': None}]

    for i, ingredient in enumerate(ingredients):
        ingredient_components.append(ingredient_input(food=ingredient['food'], quantity=ingredient['quantity'], units=ingredient['units'], index=i))
        
    instruction_components = []
    if instructions is None:
        instructions = [{'instruction': None, 'image': None}]

    for i, instruction in enumerate(instructions):
        instruction_components.append(instruction_input(instruction=instruction['instruction'], image=instruction['image'], index=i))


    return dbc.Container([
        html.H1('Create Recipe', className='text-center'),
        dbc.Row([
            dbc.Col([
                # main image upload
                main_image_upload(image=main_image),
            ], width=3),
            dbc.Col([
                # Category: dropdown of categories
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Category'),
                        dbc.Select(
                            id='category-select',
                            options=[
                                {'label': 'Breakfast', 'value': 'breakfast'},
                                {'label': 'Lunch', 'value': 'lunch'},
                                {'label': 'Dinner', 'value': 'dinner'},
                                {'label': 'Dessert', 'value': 'dessert'},
                                {'label': 'Snack', 'value': 'snack'},
                                {'label': 'Drink', 'value': 'drink'},
                            ],
                            value=category,
                        ),
                    ]),
                ], className='mb-3'),
                # Food name: inline text input
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Food name'),
                        dbc.Input(
                            type='text',
                            id='food-name-input',
                            placeholder='Enter food name',
                            value=food_name,
                        ),
                    ]),
                ], className='mb-3'),
                # Servings: inline float input
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Servings'),
                        dbc.Input(
                            type='text',
                            id='servings-input',
                            placeholder='Enter number of servings',
                            value=servings,
                        ),
                    ]),
                    dbc.Col([
                        dbc.Label('Time'),
                        dbc.Input(
                            type='text',
                            id='time-input',
                            placeholder='Enter time',
                            value=time,
                        ),
                    ]),
                ], className='mb-3'),
                dbc.Row([
                    dbc.Col([
                        # Ingredients: list of ingredient inputs
                        html.H3('Ingredients'),
                        html.Div(id='ingredients-container', children=ingredient_components),
                        dbc.Button('Add ingredient', id='add-ingredient-button'),
                    ]),
                ], className='mb-3'),
                dbc.Row([
                    dbc.Col([
                        # Instructions: list of instruction inputs
                        html.H3('Instructions'),
                        html.Div(id='instructions-container', children=instruction_components),
                        dbc.Button('Add step', id='add-step-button'),
                    ]),
                ], className='mb-3'),
                dbc.Button('Submit', id='submit-button'),
            ]),
        ]),  
    ])



layout = html.Div(create_food_form(), id='food-form')


@app.callback(
    Output('ingredients-container', 'children'),
    [
        Input('add-ingredient-button', 'n_clicks'),
        Input({'type': 'remove-ingredient-button', 'index': ALL}, 'n_clicks'),
    ],
    State('ingredients-container', 'children'),
)
def modify_ingredient_inputs(add_button_clicks, remove_button_clicks, children):
    # Get the index of the button that was clicked
    ctx = dash.callback_context
    if not ctx.triggered:
        # If no buttons have been clicked, return the current list of ingredient inputs
        return children
    else:
        triggered_id = ctx.triggered[0]['prop_id']
        print(triggered_id)
        if 'add-ingredient-button' in triggered_id:
            # If the "Add Ingredient" button was clicked, add a new input
            new_index = len(children)
            new_input = ingredient_input(index=new_index)
            children.append(new_input)
        else:
            # If a "Remove" button was clicked, remove the corresponding input
            args = json.loads(triggered_id.split('.')[0])
            index = args['index']
            children = [
                child
                for child in children
                if child['props']['id']['index'] != index
            ]

    return children



@app.callback(
    Output('instructions-container', 'children'),
    [
        Input('add-step-button', 'n_clicks'),
        Input({'type': 'remove-step-button', 'index': ALL}, 'n_clicks'),
        Input({'type': 'move-step-up-button', 'index': ALL}, 'n_clicks'),
        Input({'type': 'move-step-down-button', 'index': ALL}, 'n_clicks'),
    ],
    State('instructions-container', 'children'),
)
def modify_instruction_inputs(add_button_clicks, remove_button_clicks, move_up_clicks, move_down_clicks, children):
    # Create a dictionary to keep track of child positions
    child_positions = {}
    for i, child in enumerate(children):
        child_positions[child['props']['id']['index']] = i

    # Get the index of the button that was clicked
    ctx = dash.callback_context
    if not ctx.triggered:
        # If no buttons have been clicked, return the current list of instruction inputs
        return children
    else:
        triggered_id = ctx.triggered[0]['prop_id']
        if 'add-step-button' in triggered_id:
            # If the "Add Step" button was clicked, add a new input
            new_index = len(children)
            new_input = instruction_input(index=new_index)
            children.append(new_input)
            child_positions[new_index] = len(children) - 1
        else:
            # If a "Remove" button was clicked, remove the corresponding input
            args = json.loads(triggered_id.split('.')[0])
            index = args['index']
            if 'remove-step-button' in triggered_id:
                if index in child_positions:
                    children.pop(child_positions[index])
                    del child_positions[index]
            else:
                # If a "Move Up" or "Move Down" button was clicked, move the corresponding input
                move_direction = -1 if 'move-step-up-button' in triggered_id else 1
                if index in child_positions and 0 <= child_positions[index] + move_direction < len(children):
                    old_position = child_positions[index]
                    new_position = old_position + move_direction
                    children[old_position], children[new_position] = children[new_position], children[old_position]
                    child_positions[index] = new_position
                    child_positions[children[new_position]['props']['id']['index']] = old_position

    return children


@app.callback(
    Output('food-form', 'children'),
    Input('submit-button', 'n_clicks'),
    State('main-image-upload', 'contents'), # what type is this? answer: string, base64 encoded
    State('category-select', 'value'),
    State('food-name-input', 'value'),
    State('servings-input', 'value'),
    State('time-input', 'value'),
    State({'type': 'ingredient-name-input', 'index': ALL}, 'value'),
    State({'type': 'ingredient-quantity-input', 'index': ALL}, 'value'),
    State({'type': 'ingredient-unit-input', 'index': ALL}, 'value'),
    State({'type': 'step-input', 'index': ALL}, 'value'),
    State({'type': 'step-image-upload', 'index': ALL}, 'contents'),
    prevent_initial_call=True,
)
def save_recipe(n_clicks, main_image, category, food_name, servings, time, ingredient_names, ingredient_quantities, ingredient_units, steps, step_images):
    if n_clicks is None:
        raise PreventUpdate
    
    # Save the main image to IMAGE_FOLDER/food_name/main.jpg
    if main_image is not None:
        main_image_filename = os.path.join(IMAGE_FOLDER, food_name, 'main.jpg')
        os.makedirs(os.path.dirname(main_image_filename), exist_ok=True)
        with open(main_image_filename, 'wb') as f:
            f.write(base64.b64decode(main_image.split(',')[1]))
    else:
        main_image_filename = None


    # Create the recipe dictionary
    ingredients = [{'food': food, 'quantity': quantity, 'units': units} for food, quantity, units in zip(ingredient_names, ingredient_quantities, ingredient_units)]

    # instructions = [{'instruction': step, 'image': image} for step, image in zip(steps, step_images)]
    # save instructions images to IMAGE_FOLDER/food_name/instructions/step_index.jpg and build instructions list
    instructions = []
    for i, (step, image) in enumerate(zip(steps, step_images)):
        if image is not None:
            image_filename = os.path.join(IMAGE_FOLDER, food_name, 'instructions', f'{i}.jpg')
            os.makedirs(os.path.dirname(image_filename), exist_ok=True)
            with open(image_filename, 'wb') as f:
                f.write(base64.b64decode(image.split(',')[1]))
            instructions.append({'instruction': step, 'image': image_filename})
        else:
            instructions.append({'instruction': step, 'image': None})
    
    recipe = {
        'image': main_image_filename,
        'time': time,
        'servings': servings,
        'ingredients': ingredients,
        'instructions': instructions,
    }

    # Load the current database or create an empty one if it doesn't exist
    with open(DATABASE_FILE, 'r') as f:
        database = json.load(f)

    # Add the recipe to the database
    if category not in database:
        database[category] = {}
    database[category][food_name] = recipe

    # Save the updated database
    with open(DATABASE_FILE, 'w') as f:
        json.dump(database, f, indent=4)

    return create_food_form()


