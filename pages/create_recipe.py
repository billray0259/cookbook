import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, ALL
import dash_bootstrap_components as dbc

from globals import app


# layout = dbc.Container([
#     dbc.Row([
#         dbc.Col(html.H2('Create Recipe'), width=12)
#     ]),
#     dbc.Row([
#         dbc.Col([
#             html.Label('Name'),
#             dbc.Input(type='text', id='name-input', placeholder='Enter recipe name', className='form-control')
#         ], width=6),
#         dbc.Col([
#             html.Label('Section category'),
#             dbc.Select(
#                 options=[
#                     {'label': 'Breakfast', 'value': 'Breakfast'},
#                     {'label': 'Lunch', 'value': 'Lunch'},
#                     {'label': 'Dinner', 'value': 'Dinner'},
#                     {'label': 'Dessert', 'value': 'Dessert'},
#                     {'label': 'Drinks', 'value': 'Drinks'}
#                 ],
#                 id='section-dropdown',
#                 value='Breakfast',
#                 className='form-select'
#             )
#         ], width=6)
#     ]),
#     dbc.Row([
#         dbc.Col([
#             html.Label('Image upload'),
#             html.Div([
#                 dcc.Upload(
#                     id='upload-data',
#                     children=html.Div([
#                         'Drag and Drop or ',
#                         html.A('Select Files')
#                     ]),
#                     style={
#                         'width': '100%',
#                         'height': '60px',
#                         'lineHeight': '60px',
#                         'borderWidth': '1px',
#                         'borderStyle': 'dashed',
#                         'borderRadius': '5px',
#                         'textAlign': 'center',
#                         'margin': '10px'
#                     },
#                     # Allow multiple files to be uploaded
#                     multiple=True
#                 ),
#                 html.Div(id='output-data-upload'),
#             ]),
#             html.Div(id='output-image-upload')
#         ])
#     ]),
#     dbc.Row([
#         dbc.Col([
#             html.Label('Time to make'),
#             dbc.Input(type='text', id='time-input', placeholder='Enter time to make', className='form-control')
#         ], width=6),
#         dbc.Col([
#             html.Label('Number of servings'),
#             dbc.Input(type='text', id='servings-input', placeholder='Enter number of servings', className='form-control')
#         ], width=6)
#     ]),
#     dbc.Row([
#         dbc.Col([
#             html.H3('Ingredients'),
#             dbc.Button('Add ingredient', id='add-ingredient-button', color='primary', className='mb-3'),
#             html.Div(id='ingredients-container', children=[
#                 html.Div([
#                     dbc.Input(type='text', id={'type': 'ingredient-name-input', 'index': 0}, placeholder='Enter ingredient name', className='form-control'),
#                     dbc.Input(type='text', id={'type': 'ingredient-quantity-input', 'index': 0}, placeholder='Enter quantity', className='form-control'),
#                     dbc.Input(type='text', id={'type': 'ingredient-unit-input', 'index': 0}, placeholder='Enter unit', className='form-control'),
#                     dbc.Button('Remove', id={'type': 'remove-ingredient-button', 'index': 0}, color='danger', className='mb-3'),
#                     dbc.Button('Move up', id={'type': 'move-ingredient-up-button', 'index': 0}, color='primary', className='mb-3'),
#                     dbc.Button('Move down', id={'type': 'move-ingredient-down-button', 'index': 0}, color='primary', className='mb-3')
#                 ], id='ingredient-0', className='mb-3')
#             ])
#         ], width=6),
#         dbc.Col([
#             html.H3('Instructions'),
#             dbc.Button('Add step', id='add-step-button', color='primary', className='mb-3'),
#             html.Div(id='instructions-container', children=[
#                 html.Div([
#                     dbc.Input(type='text', id={'type': 'step-input', 'index': 0}, placeholder='Enter step', className='form-control'),
#                     html.Div([
#                         dcc.Upload(
#                             id='upload-data',
#                             children=html.Div([
#                                 'Drag and Drop or ',
#                                 html.A('Select Files')
#                             ]),
#                             style={
#                                 'width': '100%',
#                                 'height': '60px',
#                                 'lineHeight': '60px',
#                                 'borderWidth': '1px',
#                                 'borderStyle': 'dashed',
#                                 'borderRadius': '5px',
#                                 'textAlign': 'center',
#                                 'margin': '10px'
#                             },
#                             # Allow multiple files to be uploaded
#                             multiple=True
#                         ),
#                         html.Div(id='output-data-upload'),
#                     ]),
#                     dbc.Button('Remove', id={'type': 'remove-step-button', 'index': 0}, color='danger', className='mb-3'),
#                     dbc.Button('Move up', id={'type': 'move-step-up-button', 'index': 0}, color='primary', className='mb-3'),
#                     dbc.Button('Move down', id={'type': 'move-step-down-button', 'index': 0}, color='primary', className='mb-3')
#                 ], id='step-0', className='mb-3')
#             ])
#         ], width=6)
#     ]),
#     dbc.Row([
#         dbc.Col([
#             dbc.Button('Submit', id='submit-button', color='success', className='mt-5')
#         ], width=12, align='center')
#     ])
# ])


def main_image_upload(image=None):
    return html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Image')
            ]),
            className='image-upload',
            # style height = 180px
            # center text vertically
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

    return html.Div([row1, row2], className='mb-2 bg-light p-2')



def instruction_input(instruction=None, image=None, index=0):

    # first row: text input for step
    row1 = dbc.Row([
        dbc.Col(
            # dbc.Input(
            #     type='text',
            #     id={'type': 'step-input', 'index': index},
            #     placeholder='Enter step',
            #     className='form-control',
            #     value=instruction,
            # )
            # make that input a multi-line text input
            dcc.Textarea(
                id={'type': 'step-input', 'index': index},
                placeholder='Enter step',
                className='form-control',
                value=instruction,
            )
        ),
        dbc.Col([
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    html.A('Add Image (optional)')
                ]),
                className='image-upload',
                multiple=True
            ),
            html.Div(id='output-data-upload'),
        ], width=3)
    ])

    # second row: button to remove step, button to move step up, button to move step down
    # row2 = dbc.Row(
    #     [
    #         dbc.Col(
    #             dbc.Button('Remove', id={'type': 'remove-step-button', 'index': index}, color='danger'),
    #             className='mb-3',
    #         ),
    #         dbc.Col(
    #             dbc.Button('Move up', id={'type': 'move-step-up-button', 'index': index}, color='primary'),
    #             className='mb-3',
    #         ),
    #         dbc.Col(
    #             dbc.Button('Move down', id={'type': 'move-step-down-button', 'index': index}, color='primary'),
    #             className='mb-3',
    #         ),
    #     ],
    #     className='justify-content-between',
    # )

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

    # return html.Div([row1, row2], className='mb-2 bg-light')
    # add a className to add padding
    return html.Div([row1, row2], className='mb-2 bg-light p-2')




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



layout = create_food_form()





# # Define the callbacks for the form inputs
# @app.callback(
#     Output('ingredients-container', 'children'),
#     [Input('add-ingredient-button', 'n_clicks')],
#     [State('ingredients-container', 'children')]
# )
# def add_ingredient(n_clicks, children):
#     new_index = len(children)
#     new_ingredient = html.Div([
#         dcc.Input(type='text', id={'type': 'ingredient-name-input', 'index': new_index}, placeholder='Enter ingredient name'),
#         dcc.Input(type='text', id={'type': 'ingredient-quantity-input', 'index': new_index}, placeholder='Enter quantity'),
#         dcc.Input(type='text', id={'type': 'ingredient-unit-input', 'index': new_index}, placeholder='Enter unit'),
#         html.Button('Remove ingredient', id={'type': 'remove-ingredient-button', 'index': new_index}),
#         html.Button('Move up', id={'type': 'move-ingredient-up-button', 'index': new_index}),
#         html.Button('Move down', id={'type': 'move-ingredient-down-button', 'index': new_index})
#     ], id=f'ingredient-{new_index}', className='ingredient')
#     children.append(new_ingredient)
#     return children

# @app.callback(
#     Output('instructions-container', 'children'),
#     [Input('add-step-button', 'n_clicks')],
#     [State('instructions-container', 'children')]
# )
# def add_step(n_clicks, children):
#     new_index = len(children)
#     new_step = html.Div([
#         dcc.Input(type='text', id={'type': 'step-input', 'index': new_index}, placeholder='Enter step'),
#         dcc.Upload(
#             id={'type': 'step-image-upload', 'index': new_index},
#             children=html.Div([
#                 'Drag and drop or click to select a file'
#             ]),
#             style={
#                 'width': '100%',
#                 'height': '60px',
#                 'lineHeight': '60px',
#                 'borderWidth': '1px',
#                 'borderStyle': 'dashed',
#                 'borderRadius': '5px',
#                 'textAlign': 'center'
#             },
#             multiple=False
#         ),
#         html.Button('Remove step', id={'type': 'remove-step-button', 'index': new_index}),
#         html.Button('Move up', id={'type': 'move-step-up-button', 'index': new_index}),
#         html.Button('Move down', id={'type': 'move-step-down-button', 'index': new_index})
#     ], id=f'step-{new_index}', className='step')
#     children.append(new_step)
#     return children

# @app.callback(
#     Output('ingredients-container', 'children'),
#     [
#         Input({'type': 'remove-ingredient-button', 'index': ALL}, 'n_clicks'),
#         Input({'type': 'move-ingredient-up-button', 'index': ALL}, 'n_clicks'),
#         Input({'type': 'move-ingredient-down-button', 'index': ALL}, 'n_clicks')
#     ],
#     [State('ingredients-container', 'children')]
# )
# def update_ingredients(n_clicks_remove, n_clicks_up, n_clicks_down, children):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         return children
#     else:
#         button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#         button_type = button_id.split('-')[0]
#         index = int(button_id.split('-')[1])
#         if button_type == 'remove':
#             children.pop(index)
#         elif button_type == 'move':
#             if 'up' in button_id:
#                 if index > 0:
#                     children[index], children[index-1] = children[index-1], children[index]
#             elif 'down' in button_id:
#                 if index < len(children)-1:
#                     children[index], children[index+1] = children[index+1], children[index]
#     return children

# @app.callback(
#     Output('instructions-container', 'children'),
#     [
#         Input({'type': 'remove-step-button', 'index': ALL}, 'n_clicks'),
#         Input({'type': 'move-step-up-button', 'index': ALL}, 'n_clicks'),
#         Input({'type': 'move-step-down-button', 'index': ALL}, 'n_clicks')
#     ],
#     [State('instructions-container', 'children')]
# )
# def update_steps(n_clicks_remove, n_clicks_up, n_clicks_down, children):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         return children
#     else:
#         button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#         button_type = button_id.split('-')[0]
#         index = int(button_id.split('-')[1])
#         if button_type == 'remove':
#             children.pop(index)
#         elif button_type == 'move':
#             if 'up' in button_id:
#                 if index > 0:
#                     children[index], children[index-1] = children[index-1], children[index]
#             elif 'down' in button_id:
#                 if index < len(children)-1:
#                     children[index], children[index+1] = children[index+1], children[index]
#     return children

# @app.callback(
#     Output('name-input', 'value'),
#     [Input('submit-button', 'n_clicks')],
#     [
#         State('name-input', 'value'),
#         State('section-dropdown', 'value'),
#         State('image-upload', 'filename'),
#         State('image-upload', 'contents'),
#         State('time-input', 'value'),
#         State('servings-input', 'value'),
#         State({'type': 'ingredient-name-input', 'index': ALL}, 'value'),
#         State({'type': 'ingredient-quantity-input', 'index': ALL}, 'value'),
#         State({'type': 'ingredient-unit-input', 'index': ALL}, 'value'),
#         State({'type': 'step-input', 'index': ALL}, 'value'),
#         State({'type': 'step-image-upload', 'index': ALL}, 'filename'),
#         State({'type': 'step-image-upload', 'index': ALL}, 'contents'),
#     ]
# )
# def save_recipe(n_clicks, name, section, image_filename, image_contents, time, servings, ingredient_names, ingredient_quantities, ingredient_units, step_text, step_image_filenames, step_image_contents):
#     if n_clicks is not None:
#         # Save the recipe to the database
#         # ...
        
#         # Clear the form inputs
#         return ''
#     else:
#         return name
