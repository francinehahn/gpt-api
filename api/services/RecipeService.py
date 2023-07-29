"""Recipe service"""
import os
import uuid
from mysql.connector import Error
import openai
from dotenv import load_dotenv
from marshmallow import ValidationError
from api.schema.RecipeSchema import RecipeSchema
from api.errors.RecipeErrors import RecipeNotFound

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class RecipeService:
    """This class receives data from the controller and returns the response from the open ai api"""

    def __init__(self, recipe_database, authentication):
        self.recipe_database = recipe_database
        self.authentication = authentication

    def create_recipe(self, data):
        """This method receives ingredients and returns a recipe"""
        try:
            RecipeSchema().load(data)

            user_id = self.authentication.get_identity()
            recipe_id = str(uuid.uuid4())

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Crie uma receita com os seguintes ingredientes: {data['ingredients']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )
            
            self.recipe_database.create_recipe(recipe_id, data['ingredients'], response['choices'][0]['text'], user_id)

            return response['choices'][0]['text']
        
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