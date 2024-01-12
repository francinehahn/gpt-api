"""Recipe service"""
import uuid
from marshmallow import ValidationError
from botocore.exceptions import ClientError
from api.schema.RecipeSchema import RecipeSchema
from api.errors.RecipeErrors import RecipeNotFound
from api.errors.RecipeErrors import NoRecipesToUpdate
from api.utils.current_datetime import current_time

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
            created_at = current_time()
            response = self.open_ai.generate_recipe(data['ingredients'])
            data_db = {
                'recipe_id': recipe_id, 
                'ingredients': data['ingredients'], 
                'answer': response, 
                'user_id': user_id, 
                'created_at': created_at
            }
            self.recipe_database.create_recipe(data_db)
            return response
        except ValidationError as err:
            raise err
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
        
    def get_recipes(self):
        """This method receives a token and sends the user_id to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            recipes = self.recipe_database.get_recipes(user_id)

            response = []
            for recipe in recipes['Items']:
                response.append({
                    "id": recipe[0],
                    "question": recipe[1],
                    "answer": recipe[2],
                    "user_id": recipe[3],
                    "created_at": recipe[4]
                })
            return response
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
        
    def delete_recipe_by_id(self, recipe_id):
        """This method receives a recipe_id and a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            recipe = self.recipe_database.get_recipe_by_id(recipe_id)
        
            if 'Item' not in recipe:
                raise RecipeNotFound("Recipe not found.")

            self.recipe_database.delete_recipe_by_id(recipe_id)
        except RecipeNotFound as err:
            raise err
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
        
    def regenerate_recipe(self):
        """This method receives a a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            all_recipes = self.recipe_database.get_recipes(user_id)
            if 'Items' in all_recipes and len(all_recipes['Items']) == 0:
                raise NoRecipesToUpdate("There are no recipes registered in the database.")

            all_recipes = all_recipes['Items']
            last_recipe = all_recipes[-1]
            recipe_id = last_recipe[0]
            question = last_recipe[1] #ingredients

            response = self.open_ai.generate_recipe(question)
            self.recipe_database.regenerate_recipe({'answer': response, 'recipe_id': recipe_id})
        except NoRecipesToUpdate as err:
            raise err
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
        