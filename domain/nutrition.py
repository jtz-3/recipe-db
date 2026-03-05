# Calculations to obtain nutritional info of a recipe
# per base serving.

import sqlite3

class NutritionInfo:
    def __init__(self, recipeId):
        self.recipeId = str(recipeId)
        self.nutrient_cols = {'protein': 'ProteinPerGram',
                              'fat': 'FatPerGram',
                              'calories': 'CaloriesPerGram',
                              'fiber': 'FiberPerGram'}

    # Yes I know calories are not nutrients
    def get_info(self, nutrients):
        query = "SELECT SUM(ri.QuantityInGrams * i." + self.nutrient_cols[nutrient] + ") \
                FROM RecipeIngredient ri \
                JOIN Ingredient i ON ri.IngredientId = i.Id \
                WHERE ri.RecipeId = ?;"
        
        # Should we be checking here if the DB has been made?
        with sqlite3.connect('../db/recipes.db') as conn:
            cur = conn.cursor()
            cur.execute(query, (self.recipeId))
            row = cur.fetchone()            # Later change to .fetchall if support for multiple nutrients added
            cur.close()

        return row