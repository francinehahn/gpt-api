"""Summary database"""
from mysql.connector import connect, Error
from api.connectionDb.ConnectionDb import config

class SummaryDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""

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

    def get_summary_by_id(self, user_id, summary_id):
        """This method receives a user_id and a summary_id and returns the summary"""
        try:
            connection = connect(**config)
            cursor = connection.cursor()
            query = "SELECT * FROM summary_gpt WHERE user_id = (%s) AND id = (%s)"
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
            query = "DELETE FROM summary_gpt WHERE user_id = (%s) AND id = (%s)"
            values = (user_id, summary_id)
            cursor.execute(query, values)
            connection.commit()

        except Error as err:
            raise err
        finally:
            cursor.close()
            connection.close()