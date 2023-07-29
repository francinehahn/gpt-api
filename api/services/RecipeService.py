"""Recipe service"""
import uuid
from mysql.connector import Error
from marshmallow import ValidationError
from api.schema.RecipeSchema import RecipeSchema
from api.errors.RecipeErrors import RecipeNotFound
from api.errors.RecipeErrors import NoRecipesToUpdate

class RecipeService:
    """This class receives data from the controller and returns the response from the open ai api"""

    def __init__(self, recipe_database, authentication, open_ai):
        self.recipe_database = recipe_database
        self.authentication = authentication
        self.open_ai = open_ai

    def create_recipe(self, data):
        """This method receives ingredients and returns a recipe"""
        try:
            RecipeSchema().load(data)
            user_id = self.authentication.get_identity()
            recipe_id = str(uuid.uuid4())

            response = self.open_ai.generate_recipe(data['ingredients'])
            self.recipe_database.create_recipe(recipe_id, data['ingredients'], response, user_id)
            return response
        
        except ValidationError as err:
            raise err
        except Error as err:
            raise err
        
    def get_recipes(self):
        """This method receives a token and sends the user_id to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            recipes = self.recipe_database.get_recipes(user_id)

            response = []
            for recipe in recipes:
                response.append({
                    "id": recipe[0],
                    "question": recipe[1],
                    "answer": recipe[2],
                    "user_id": recipe[3]
                })
            
            return response
        
        except Error as err:
            raise err
        
    def delete_recipe_by_id(self, recipe_id):
        """This method receives a recipe_id and a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            recipe = self.recipe_database.get_recipe_by_id(user_id, recipe_id)
        
            if recipe is None:
                raise RecipeNotFound("Recipe not found.")

            self.recipe_database.delete_recipe_by_id(user_id, recipe_id)
        
        except RecipeNotFound as err:
            raise err
        except Error as err:
            raise err
        
    def regenerate_recipe(self):
        """This method receives a a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            all_recipes = self.recipe_database.get_recipes(user_id)
            if len(all_recipes) == 0:
                raise NoRecipesToUpdate("There are no recipes registered in the database.")

            last_recipe = all_recipes[-1]
            recipe_id = last_recipe[0]
            question = last_recipe[1] #ingredients

            response = self.open_ai.generate_recipe(question)
            self.recipe_database.regenerate_recipe(response, user_id, recipe_id)
        
        except NoRecipesToUpdate as err:
            raise err
        except Error as err:
            raise err