"""Summary database"""
from mysql.connector import connect, Error
from api.connectionDb.ConnectionDb import config

class SummaryDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""
    TABLE_NAME = "summary_gpt"

    def create_summary(self, summary_id, text, answer, user_id, created_at):
        """This method receives the summary from the service layer and inserts it into the database"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"INSERT INTO {self.TABLE_NAME} (id, question, answer, user_id, created_at) VALUES (%s, %s, %s, %s, %s)"
            values = (summary_id, text, answer, user_id, created_at)
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
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE user_id = (%s) ORDER BY created_at ASC"
            cursor.execute(query, (user_id,))
            summaries = cursor.fetchall()
            return summaries
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def get_summary_by_id(self, user_id, summary_id):
        """This method receives a user_id and a summary_id and returns the summary"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE user_id = (%s) AND id = (%s)"
            values = (user_id, summary_id)
            cursor.execute(query, values)
            summary = cursor.fetchone()
            return summary
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def delete_summary_by_id(self, user_id, summary_id):
        """This method receives a user_id and a summary_id and deletes the summary"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"DELETE FROM {self.TABLE_NAME} WHERE user_id = (%s) AND id = (%s)"
            values = (user_id, summary_id)
            cursor.execute(query, values)
            connection.commit()
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()

    def regenerate_summary(self, answer, user_id, summary_id):
        """This method receives a user_id, a summary_id, and a new answer and updates the summary (answer)"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = f"UPDATE {self.TABLE_NAME} SET answer = (%s) WHERE user_id = (%s) AND id = (%s)"
            values = (answer, user_id, summary_id)
            cursor.execute(query, values)
            connection.commit()
        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()
            