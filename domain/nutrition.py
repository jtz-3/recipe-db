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
    
    def __init__(self, calories, protein, carbs, fat, fiber, servings):
        self.servings = servings
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.fiber = fiber
    
    # To initialize a NutritionInfo object from DB values.
    def from_recipe(recipeId):
        # Create aggregation query to compute macros
        agg = ['SUM(ri.QuantityInGrams * i.' + col + ')' for col in NutritionInfo.nutrient_cols.values()]
        agg = ', '.join(agg)

        nutrient_query = 'SELECT ' + agg + ' FROM RecipeIngredient ri \
                JOIN Ingredient i ON ri.IngredientId = i.Id \
                WHERE ri.RecipeId = ?;'
        
        with sqlite3.connect('../db/recipes.db') as conn:
            cur = conn.cursor()
            cur.execute(nutrient_query, (recipeId,))
            calories, protein, carbs, fat, fiber = cur.fetchone()

            # Set serving size
            cur.execute('SELECT BaseServings FROM Recipe WHERE Id = ?', (recipeId,))
            servings = cur.fetchone()[0]
            cur.close()
        
        return NutritionInfo(calories, protein, carbs, fat, fiber, servings)
    
    # Return a new NutritionInfo object scaled to the desired number of servings.
    def scale(self, desired_servings):
        base_servings = self.servings
        ratio = desired_servings / base_servings

        return NutritionInfo(self.calories * ratio, self.protein * ratio, self.carbs * ratio,
                             self.fat * ratio, self.fiber * ratio, desired_servings)