# For now assume markdown is located in the recipe_db folder (later can
# get user specification for correct Obsidian vault)
import sqlite3
"""
Also need:
- Ingredients separation? (Sauce: ...., Dough: ....)
- Prep time: (Widget with min/hr etc)
- Step separation (cf. ingredient separation)

- Callouts for preparation or smth 
"""

def generate_markdown(recipeId):
    # What we need to convert to markdown.
    description = ''
    ingredients = ''
    steps = ''
    notes = ''
    nutrition = ''

    # Retrieve DB information to populate markdown fields
    with sqlite3.connect('../db/recipes.db') as conn:
        cur = conn.cursor()


        cur.execute('SELECT Description, Steps, Notes, BaseServings FROM Recipe WHERE Id = ?', (recipeId,))
        description, steps, notes, servings = cur.fetchone()

        # To get ingredietns we have to do something more sophisticated (join tables)
        cur.execute('SELECT i.Name, ri.Quantity, ri.Unit \
                    FROM Ingredient i \
                    JOIN RecipeIngredient ri ON i.Id = ri.IngredientId \
                    WHERE ri.RecipeId = ?', (recipeId,))
        
        # List of results.
        ingredients = cur.fetchall()
        cur.close()

    # TEST:
    print(description, steps, notes, servings, ingredients)

    # Modify the text for proper output


    # Create and write to the markdown file.
    # with open('../markdown_test.md', 'w') as markdown:
    #     markdown.write('# Header \n')
    #     markdown.write('## Next header \n')
    #     markdown.write('# Header2')
    #     # File writing in general goes here

    # return

# TEST
generate_markdown(1)




