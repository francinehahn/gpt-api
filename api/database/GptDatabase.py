from api.connection_db.connection_db import config
from flask import jsonify, request
from mysql.connector import connect

class GptDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""

    def create_recipe(self, id, ingredients, answer, user_id):
        """This method receives the recipe from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "INSERT INTO recipes_gpt (id, question, answer, user_id) VALUES (%s, %s, %s, %s)"
            values = (id, ingredients, answer, user_id)
            cursor.execute(query, values)
            connection.commit()

        except Exception as err:
            response =  jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        finally:
            cursor.close()
            connection.close()

    def create_summary(self, id, text, answer, user_id):
        """This method receives the summary from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "INSERT INTO summary_gpt (id, question, answer, user_id) VALUES (%s, %s, %s, %s)"
            values = (id, text, answer, user_id)
            cursor.execute(query, values)
            connection.commit()

        except Exception as err:
            response =  jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        finally:
            cursor.close()
            connection.close()

    def translator(self, id, text, answer, user_id):
        """This method receives the translation from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "INSERT INTO translator_gpt (id, question, answer, user_id) VALUES (%s, %s, %s, %s)"
            values = (id, text, answer, user_id)
            cursor.execute(query, values)
            connection.commit()

        except Exception as err:
            response =  jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        finally:
            cursor.close()
            connection.close()

    def writing_assistant(self, id, text, answer, user_id):
        """This method receives the text from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "INSERT INTO writing_assistant_gpt (id, question, answer, user_id) VALUES (%s, %s, %s, %s)"
            values = (id, text, answer, user_id)
            cursor.execute(query, values)
            connection.commit()

        except Exception as err:
            response =  jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        finally:
            cursor.close()
            connection.close()