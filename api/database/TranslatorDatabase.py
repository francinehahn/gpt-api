"""Translator database"""
from mysql.connector import connect, Error
from api.connectionDb.ConnectionDb import config

class TranslatorDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""

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