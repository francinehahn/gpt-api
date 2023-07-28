"""Text service"""
import os
import uuid
from mysql.connector import Error
import openai
from dotenv import load_dotenv
from marshmallow import ValidationError
from api.schema.WritingAssistantSchema import WritingAssistantSchema
from api.errors.TextErrors import TextNotFound

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class TextService:
    """This class receives data from the controller and returns the response from the open ai api"""

    def __init__(self, text_database, authentication):
        self.text_database = text_database
        self.authentication = authentication

    def create_text(self, data):
        """This method receives the subject of a text and returns the text"""
        try:
            WritingAssistantSchema().load(data)
            
            user_id = self.authentication.get_identity()
            writing_assistant_id = str(uuid.uuid4())

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Crie um texto para: {data['text']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )
            
            self.text_database.create_text(writing_assistant_id, data['text'], response['choices'][0]['text'], user_id)

            return response['choices'][0]['text']
        
        except ValidationError as err:
            raise err
        except Error as err:
            raise err
    
    def get_texts(self):
        """This method receives a user_id and sends it to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            texts = self.text_database.get_texts(user_id)

            response = []
            for text in texts:
                response.append({
                    "id": text[0],
                    "question": text[1],
                    "answer": text[2],
                    "user_id": text[3]
                })
            
            return response
        
        except Error as err:
            raise err
        
    def delete_text_by_id(self, text_id):
        """This method receives a text_id and a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            text = self.text_database.get_text_by_id(user_id, text_id)
        
            if text is None:
                raise TextNotFound("Text not found.")

            self.text_database.delete_text_by_id(user_id, text_id)
        
        except TextNotFound as err:
            raise err
        except Error as err:
            raise err