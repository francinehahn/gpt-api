"""Recipe database"""
from mysql.connector import connect, Error
from api.connectionDb.ConnectionDb import config

class RecipeDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""
    TABLE_NAME = "recipes_gpt"

    def create_recipe(self, recipe_id, ingredients, answer, user_id, created_at):
        """This method receives the recipe from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"INSERT INTO {self.TABLE_NAME} (id, question, answer, user_id, created_at) VALUES (%s, %s, %s, %s, %s)"
            values = (recipe_id, ingredients, answer, user_id, created_at)
            cursor.execute(query, values)
            connection.commit()
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()
    
    def get_recipes(self, user_id):
        """This method receives a user_id and returns all the recipes from the account"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE user_id = (%s) ORDER BY created_at ASC"
            cursor.execute(query, (user_id,))
            recipes = cursor.fetchall()
            return recipes
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def get_recipe_by_id(self, user_id, recipe_id):
        """This method receives a user_id and a recipe_id and returns the recipe"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE user_id = (%s) AND id = (%s)"
            values = (user_id, recipe_id)
            cursor.execute(query, values)
            recipe = cursor.fetchone()
            return recipe
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def delete_recipe_by_id(self, user_id, recipe_id):
        """This method receives a user_id and a recipe_id and deletes the recipe"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"DELETE FROM {self.TABLE_NAME} WHERE user_id = (%s) AND id = (%s)"
            values = (user_id, recipe_id)
            cursor.execute(query, values)
            connection.commit()
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def regenerate_recipe(self, answer, user_id, recipe_id):
        """This method receives a user_id, a recipe_id, and new answer and updates the recipe (answer)"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"UPDATE {self.TABLE_NAME} SET answer = (%s) WHERE user_id = (%s) AND id = (%s)"
            values = (answer, user_id, recipe_id)
            cursor.execute(query, values)
            connection.commit()
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()