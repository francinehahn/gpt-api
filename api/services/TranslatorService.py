"""Translator service"""
import os
import uuid
from mysql.connector import Error
import openai
from dotenv import load_dotenv
from marshmallow import ValidationError
from api.schema.TranslatorSchema import TranslatorSchema

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class TranslatorService:
    """This class receives data from the controller and returns the response from the open ai api"""

    def __init__(self, translator_database, authentication):
        self.translator_database = translator_database
        self.authentication = authentication
         
    def create_translation(self, data):
        """This method receives a source language, a target language and a text and returns the translation"""
        try:
            TranslatorSchema().load(data)
            
            user_id = self.authentication.get_identity()
            translator_id = str(uuid.uuid4())
            
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Traduza o seguinte texto do {data['source_language']} para o {data['target_language']}: {data['text']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )

            self.translator_database.create_translation(translator_id, data['text'], response['choices'][0]['text'], user_id)

            return response['choices'][0]['text']
        
        except ValidationError as err:
            raise err
        except Error as err:
            raise err
    
    def get_translations(self):
        """This method receives a user_id and sends it to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            translations = self.translator_database.get_translations(user_id)

            response = []
            for translation in translations:
                response.append({
                    "id": translation[0],
                    "question": translation[1],
                    "answer": translation[2],
                    "user_id": translation[3]
                })
            
            return response
        
        except Error as err:
            raise err