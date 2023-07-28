"""Summary service"""
import os
import uuid
from mysql.connector import Error
import openai
from dotenv import load_dotenv
from marshmallow import ValidationError
from api.schema.SummarySchema import SummarySchema
from api.errors.SummaryErrors import SummaryNotFound

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class SummaryService:
    """This class receives data from the controller and returns the response from the open ai api"""

    def __init__(self, summary_database, authentication):
        self.summary_database = summary_database
        self.authentication = authentication
    
    def create_summary(self, data):
        """This method receives a text and returns a summary of it"""
        try:
            SummarySchema().load(data)
            
            user_id = self.authentication.get_identity()
            summary_id = str(uuid.uuid4())

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Resuma o seguinte texto: {data['text']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )

            self.summary_database.create_summary(summary_id, data['text'], response['choices'][0]['text'], user_id)
            
            return response['choices'][0]['text']
        
        except ValidationError as err:
            raise err
        except Error as err:
            raise err

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
                    "user_id": summary[3]
                })
            
            return response
        
        except Error as err:
            raise err
        
    def delete_summary_by_id(self, summary_id):
        """This method receives a summary_id and a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            summary = self.summary_database.get_summary_by_id(user_id, summary_id)
        
            if summary is None:
                raise SummaryNotFound("Summary not found.")

            self.summary_database.delete_summary_by_id(user_id, summary_id)
        
        except SummaryNotFound as err:
            raise err
        except Error as err:
            raise err