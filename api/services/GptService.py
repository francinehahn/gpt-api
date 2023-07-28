"""Gpt service"""
import os
import uuid

from mysql.connector import Error

import openai
from dotenv import load_dotenv

from marshmallow import ValidationError

from api.schema.RecipeSchema import RecipeSchema
from api.schema.SummarySchema import SummarySchema
from api.schema.TranslatorSchema import TranslatorSchema
from api.schema.WritingAssistantSchema import WritingAssistantSchema

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class GptService:
    """This class receives data from the controller and returns the response from the open ai api"""

    def __init__(self, gpt_database, authentication):
        self.gpt_database = gpt_database
        self.authentication = authentication

    def create_recipe(self, data):
        """This method receives ingredients and returns a recipe"""
        try:
            RecipeSchema().load(data)

            user_id = self.authentication.get_identity()
            recipe_id = str(uuid.uuid4())

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Crie uma receita com os seguintes ingredientes: {data['ingredients']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )
            
            self.gpt_database.create_recipe(recipe_id, data['ingredients'], response['choices'][0]['text'], user_id)

            return response['choices'][0]['text']
        
        except ValidationError as err:
            raise err
        except Error as err:
            raise err
    
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

            self.gpt_database.create_summary(summary_id, data['text'], response['choices'][0]['text'], user_id)
            
            return response['choices'][0]['text']
        
        except ValidationError as err:
            raise err
        except Error as err:
            raise err
        
    def translator(self, data):
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

            self.gpt_database.translator(translator_id, data['text'], response['choices'][0]['text'], user_id)

            return response['choices'][0]['text']
        
        except ValidationError as err:
            raise err
        except Error as err:
            raise err
    
    def writing_assistant(self, data):
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
            
            self.gpt_database.writing_assistant(writing_assistant_id, data['text'], response['choices'][0]['text'], user_id)

            return response['choices'][0]['text']
        
        except ValidationError as err:
            raise err
        except Error as err:
            raise err