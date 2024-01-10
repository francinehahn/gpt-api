"""Recipe database"""
import os
from botocore.exceptions import ClientError
import boto3
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class RecipeDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""

    def __init__(self):
        # dybmodb client
        dynamodb_client = boto3.resource(
            'dynamodb',
            aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
            aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
            region_name='sa-east-1'
        )
        self.table_recipes = dynamodb_client.Table('recipes_gpt')
        
    def create_recipe(self, data):
        """This method receives the recipe from the service layer and inserts it into the database"""
        try:
            self.table_recipes.put_item(
                Item={
                    'id': data['recipe_id'],
                    'ingredients': data['ingredients'],
                    'answer': data['answer'],
                    'user_id': data['user_id'],
                    'created_at': data['created_at']
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
    
    def get_recipes(self, user_id):
        """This method receives a user_id and returns all the recipes from the account"""
        try:
            recipes = self.table_recipes.scan(
                FilterExpression='user_id = :val',
                ExpressionAttributeValues={':val': user_id}
            )
            return recipes
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def get_recipe_by_id(self, recipe_id):
        """This method receives a user_id and a recipe_id and returns the recipe"""
        try:
            recipe = self.table_recipes.get_item(
                Key={
                    'id': recipe_id
                }
            )
            return recipe
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def delete_recipe_by_id(self, recipe_id):
        """This method receives a user_id and a recipe_id and deletes the recipe"""
        try:
            self.table_recipes.delete_item(
                Key={
                    'id': recipe_id
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def regenerate_recipe(self, data):
        """This method receives a user_id, a recipe_id, and new answer and updates the recipe (answer)"""
        try:
            self.table_recipes.update_item(
                Key={
                    'id': data['recipe_id']
                },
                UpdateExpression='SET answer = :update',
                ExpressionAttributeValues={
                    ':update': data['answer']
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
