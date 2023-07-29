"""Translator database"""
from mysql.connector import connect, Error
from api.connectionDb.ConnectionDb import config

class TranslatorDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""
    TABLE_NAME = "translator_gpt"

    def create_translation(self, translator_id, text, answer, user_id):
        """This method receives the translation from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"INSERT INTO {self.TABLE_NAME} (id, question, answer, user_id) VALUES (%s, %s, %s, %s)"
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
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE user_id = (%s)"
            cursor.execute(query, (user_id,))
            translations = cursor.fetchall()
            return translations
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def get_translation_by_id(self, user_id, translation_id):
        """This method receives a user_id and a translation_id and returns the translation"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE user_id = (%s) AND id = (%s)"
            values = (user_id, translation_id)
            cursor.execute(query, values)
            translation = cursor.fetchone()
            return translation
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def delete_translation_by_id(self, user_id, translation_id):
        """This method receives a user_id and a translation_id and deletes the translation"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"DELETE FROM {self.TABLE_NAME} WHERE user_id = (%s) AND id = (%s)"
            values = (user_id, translation_id)
            cursor.execute(query, values)
            connection.commit()
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def regenerate_translation(self, answer, user_id, translation_id):
        """This method receives a user_id, a translation_id, and a new answer and updates the translation (answer)"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"UPDATE {self.TABLE_NAME} SET answer = (%s) WHERE user_id = (%s) AND id = (%s)"
            values = (answer, user_id, translation_id)
            cursor.execute(query, values)
            connection.commit()
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()