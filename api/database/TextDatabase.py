"""Text database"""
from mysql.connector import connect, Error
from api.connectionDb.ConnectionDb import config

class TextDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""
    TABLE_NAME = "writing_assistant_gpt"

    def create_text(self, writing_assistant_id, text, answer, user_id):
        """This method receives the text from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"INSERT INTO {self.TABLE_NAME} (id, question, answer, user_id) VALUES (%s, %s, %s, %s)"
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
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE user_id = (%s)"
            cursor.execute(query, (user_id,))
            texts = cursor.fetchall()
            return texts
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def get_text_by_id(self, user_id, text_id):
        """This method receives a user_id and a text_id and returns the text"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE user_id = (%s) AND id = (%s)"
            values = (user_id, text_id)
            cursor.execute(query, values)
            text = cursor.fetchone()
            return text
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def delete_text_by_id(self, user_id, text_id):
        """This method receives a user_id and a text_id and deletes the text"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"DELETE FROM {self.TABLE_NAME} WHERE user_id = (%s) AND id = (%s)"
            values = (user_id, text_id)
            cursor.execute(query, values)
            connection.commit()
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def regenerate_text(self, answer, user_id, text_id):
        """This method receives a user_id, a text_id, and a new answer and updates the text (answer)"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"UPDATE {self.TABLE_NAME} SET answer = (%s) WHERE user_id = (%s) AND id = (%s)"
            values = (answer, user_id, text_id)
            cursor.execute(query, values)
            connection.commit()
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()