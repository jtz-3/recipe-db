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
        self.recipeId = recipeId
        self.base_servings = None

        # Initialize all nutrition info and set class values. 
        agg = ['SUM(ri.QuantityInGrams * i.' + col + ')' for col in NutritionInfo.nutrient_cols.values()]
        agg = ', '.join(agg)

        nutrient_query = 'SELECT ' + agg + 'FROM RecipeIngredient ri \
                JOIN Ingredient i ON ri.IngredientId = i.Id \
                WHERE ri.RecipeId = ?;'
        
        # Should we be checking here if the DB has been made?
        # CHECK ABOUT FETCHALL, FETCHONE METHODS
        with sqlite3.connect('../db/recipes.db') as conn:
            cur = conn.cursor()
            cur.execute(nutrient_query, (self.recipeId,))
            self.calories, self.protein, self.carbs, self.fat, self.fiber = cur.fetchall()[0]

            cur.execute('SELECT BaseServings FROM Recipe WHERE Id = ?', (self.recipeId))
            self.base_servings = cur.fetchone()[0]
            cur.close()

    # Provide a dictionary to update totals with, e.g.
    # {'protein': 16.0, 'fiber': 2.0} 
    def set_macros(self, nutrients):
        for macro,val in nutrients.items():
            setattr(self, macro, val)
    
    # Return a new NutritionInfo object scaled to the desired number of servings.
    def scale(self, desired_servings):
        scaled_meal = NutritionInfo(self.recipeId)
        ratio = desired_servings / self.base_servings
        scaled_meal.set_macros({'protein': scaled_meal.protein * ratio,
                                'calories': scaled_meal.calories * ratio,
                                'carbs': scaled_meal.carbs * ratio,
                                'fat': scaled_meal.fat * ratio,
                                'fiber': scaled_meal.fiber * ratio})

        return scaled_meal