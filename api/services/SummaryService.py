"""Summary service"""
import uuid
from botocore.exceptions import ClientError
from marshmallow import ValidationError
from api.schema.SummarySchema import SummarySchema
from api.errors.SummaryErrors import SummaryNotFound
from api.errors.SummaryErrors import NoSummariesToUpdate
from api.utils.current_datetime import current_time

class SummaryService:
    """This class receives data from the controller and returns the response from the open ai api"""
    def __init__(self, summary_database, authentication, open_ai):
        self.summary_database = summary_database
        self.authentication = authentication
        self.open_ai = open_ai
    
    def create_summary(self, data):
        """This method receives a text and returns a summary of it"""
        try:
            SummarySchema().load(data)
            user_id = self.authentication.get_identity()
            summary_id = str(uuid.uuid4())
            created_at = current_time()

            response = self.open_ai.generate_summary(data['text'])
            data_db = {
                'summary_id': summary_id, 
                'text': data['text'], 
                'answer': response, 
                'user_id': user_id, 
                'created_at': created_at
            }
            self.summary_database.create_summary(data_db)
            return response
        except ValidationError as err:
            raise err
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def get_summaries(self):
        """This method receives a token and sends the user_id to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            summaries = self.summary_database.get_summaries(user_id)

            response = []
            for summary in summaries:
                response.append({
                    "id": summary[0],
                    "question": summary[1],
                    "answer": summary[2],
                    "user_id": summary[3],
                    "created_at": summary[4]
                })
            return response
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
        
    def delete_summary_by_id(self, summary_id):
        """This method receives a summary_id and a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            summary = self.summary_database.get_summary_by_id(summary_id)
            if summary is None:
                raise SummaryNotFound("Summary not found.")

            self.summary_database.delete_summary_by_id(summary_id)
        except SummaryNotFound as err:
            raise err
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
        
    def regenerate_summary(self):
        """This method receives a a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            all_summaries = self.summary_database.get_summaries(user_id)
            if len(all_summaries) == 0:
                raise NoSummariesToUpdate("There are no summaries registered in the database.")

            last_summary = all_summaries[-1]
            summary_id = last_summary[0]
            question = last_summary[1]

            response = self.open_ai.generate_summary(question)
            data_db = {
                'summary_id': summary_id,
                'answer': response
            }
            self.summary_database.regenerate_summary(data_db)
        except NoSummariesToUpdate as err:
            raise err
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
        