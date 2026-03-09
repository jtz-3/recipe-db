# Calculations to obtain nutritional info of a recipe
# per base serving.
import sqlite3

class NutritionInfo:
    nutrient_cols = {'calories': 'CaloriesPerGram',
                    'protein': 'ProteinPerGram',
                    'carbs': 'CarbsPerGram',
                    'fat': 'FatPerGram',
                    'fiber': 'FiberPerGram',
                    }

    def __init__(self, recipeId):
        self.recipeId = str(recipeId)
        self.base_servings = None

        # Initialize all nutrition info and set class values. 
        agg = ['SUM(ri.QuantityInGrams * i.' + col + ')' for col in NutritionInfo.nutrient_cols.values()]
        agg = ','.join(agg)
        print(agg)

        nutrient_query = 'SELECT ' + agg + 'FROM RecipeIngredient ri \
                JOIN Ingredient i ON ri.IngredientId = i.Id \
                WHERE ri.RecipeId = ?;'
        
        # Should we be checking here if the DB has been made?
        with sqlite3.connect('../db/recipes.db') as conn:
            cur = conn.cursor()
            cur.execute(nutrient_query, (self.recipeId))
            self.calories, self.protein, self.carbs, self.fat, self.fiber = cur.fetchall()[0]

            cur.execute('SELECT BaseServings FROM Recipe WHERE Id = ?', (self.recipeId))
            self.base_servings = cur.fetchone()[0]
            cur.close()

        # print('BASE SERVINGS:', self.base_servings)
        # print('MACROS:', self.calories, self.protein, self.carbs, self.fat, self.fiber)

    def get_info(self, nutrients):
        return
    
    # Return a new NutritionInfo object scaled to the desired number of servings.
    def scale(self, desired_servings):
        scaled_meal = NutritionInfo(self.recipeId)
        return scaled_meal