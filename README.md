# Read

Sections
* Breakfast
* Lunch
* Dinner
* Drinks

Possible ways to display sections
1. Dropdown
2. Tabs
3. Expanding sidebar

Section page (eg Breakfast)
* Grid of cards with breakfast recipes
    * Name
    * Image
    * Time to make
    * All ingredients

Recipe page
* Name
* Image
* Text input for desired number of servings
* All ingredients with quantities depending on number of servings
* Instructions
* Edit Recipe button


Create Recipe
Form
* Name
* Section category
* Image
* Time to make
* Ingredients [
    * Name
    * Quantity
    * number of servings
] (Button to add additional ingredient)
* Instructions [
    * Step
    * Image (optional)
] (Button to add additional step)


Edit Recipe
Populate form with recipe data
Submit form to update recipe


Database JSON
* Section Name [
    * Recipe Name
        * image (file name)
        * Time to make (string)
        * Servings (int)
        * [
            * Ingredient Name (string)
            * Quantity (float)
            * Unit (string)
        * Instructions [
            * Step
            * Image (optional)
        ]
]


# Pages

## Home Page
* Picture and navigation menu
* Navigation menu
    * Breakfast
    * Lunch
    * Dinner
    * Dessert
    * Drinks
    * Create Recipe

## Section Page
* Grid of cards with recipes

## Recipe Page
* Name (unique between recipes)
* Edit Recipe button
* Image
* Text input for desired number of servings
* All ingredients with quantities depending on number of servings
* Instructions


## Create/Edit Recipe
* Form
    * Name (text input)
    * Section category (dropdown)
    * Image upload (file input)
    * Time to make (text input)
    * Number of servings (text input)
    * Ingredients [
        * Name (text input)
        * Quantity (text input)
        * Remove ingredient button
        * Reorder ingredient button
    ] (Button to add additional ingredient)
    * Instructions [
        * Step (text input)
        * Image (optional) (file input)
        * Remove step button
        * Reorder step button
    ] (Button to add additional step)
