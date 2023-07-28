"""Gpt database"""
from mysql.connector import connect, Error
from api.connectionDb.ConnectionDb import config

class GptDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""

    def create_recipe(self, recipe_id, ingredients, answer, user_id):
        """This method receives the recipe from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "INSERT INTO recipes_gpt (id, question, answer, user_id) VALUES (%s, %s, %s, %s)"
            values = (recipe_id, ingredients, answer, user_id)
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
            query = "SELECT * FROM recipes_gpt WHERE user_id = (%s)"
            cursor.execute(query, (user_id,))
            recipes = cursor.fetchall()
            return recipes

        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def create_summary(self, summary_id, text, answer, user_id):
        """This method receives the summary from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "INSERT INTO summary_gpt (id, question, answer, user_id) VALUES (%s, %s, %s, %s)"
            values = (summary_id, text, answer, user_id)
            cursor.execute(query, values)
            connection.commit()

        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def get_summaries(self, user_id):
        """This method receives a user_id and returns all the summaries from the account"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "SELECT * FROM summary_gpt WHERE user_id = (%s)"
            cursor.execute(query, (user_id,))
            summaries = cursor.fetchall()
            return summaries

        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def create_translation(self, translator_id, text, answer, user_id):
        """This method receives the translation from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "INSERT INTO translator_gpt (id, question, answer, user_id) VALUES (%s, %s, %s, %s)"
            values = (translator_id, text, answer, user_id)
            cursor.execute(query, values)
            connection.commit()

        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def get_translations(self, user_id):
        """This method receives a user_id and returns all the translations from the account"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "SELECT * FROM translator_gpt WHERE user_id = (%s)"
            cursor.execute(query, (user_id,))
            translations = cursor.fetchall()
            return translations

        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def create_text(self, writing_assistant_id, text, answer, user_id):
        """This method receives the text from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "INSERT INTO writing_assistant_gpt (id, question, answer, user_id) VALUES (%s, %s, %s, %s)"
            values = (writing_assistant_id, text, answer, user_id)
            cursor.execute(query, values)
            connection.commit()

        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def get_texts(self, user_id):
        """This method receives a user_id and returns all the texts from the account"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "SELECT * FROM writing_assistant_gpt WHERE user_id = (%s)"
            cursor.execute(query, (user_id,))
            texts = cursor.fetchall()
            return texts

        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()