# Calculations to obtain nutritional info of a recipe
# per base serving.

import sqlite3

class NutritionInfo:
    def __init__(self, recipeId):
        self.recipeId = str(recipeId)
        self.nutrient_cols = {'protein': 'ProteinPerGram',
                              'fat': 'FatPerGram',
                              'calories': 'CaloriesPerGram',
                              'fiber': 'FiberPerGram',
                              'carbs': 'CarbsPerGram'}

    # Yes I know calories are not nutrients
    # Indicate a list of nutrients; returns a tuple of 
    # quantities (g or cal) in the corresponding order.
    def get_info(self, nutrients):
        # Turn quantity list into a series of aggregate queries
        agg = ['SUM(ri.QuantityInGrams * i.' + self.nutrient_cols[n] + ')' for n in nutrients]
        agg = ','.join(agg)

        query = 'SELECT ' + agg + 'FROM RecipeIngredient ri \
                JOIN Ingredient i ON ri.IngredientId = i.Id \
                WHERE ri.RecipeId = ?;'
        
        # Should we be checking here if the DB has been made?
        with sqlite3.connect('../db/recipes.db') as conn:
            cur = conn.cursor()
            cur.execute(query, (self.recipeId))
            rows = cur.fetchall()
            cur.close()

        return rows[0]