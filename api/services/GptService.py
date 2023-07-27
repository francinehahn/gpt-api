import openai
from dotenv import load_dotenv
import os
import uuid
from api.database.GptDatabase import GptDatabase

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class GptService:
    """This class receives data from the controller and returns the response from the open ai api"""

    def __init__(self):
        self.gpt_database = GptDatabase()

    def create_recipe(self, data):
        """This method receives ingredients and returns a recipe"""
        try:
            id = str(uuid.uuid4())

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Crie uma receita com os seguintes ingredientes: {data['ingredients']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )
            
            self.gpt_database.create_recipe(id, data['ingredients'], response['choices'][0]['text'], data['user_id'])

            return response['choices'][0]['text']
        
        except Exception as err:
            return str(err)
    
    def create_summary(self, data):
        """This method receives a text and returns a summary of it"""
        try:
            id = str(uuid.uuid4())

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Resuma o seguinte texto: {data['text']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )

            self.gpt_database.create_summary(id, data['text'], response['choices'][0]['text'], data['user_id'])
            
            return response['choices'][0]['text']
        
        except Exception as err:
            return str(err)
        
    def translator(self, data):
        """This method receives a source language, a target language and a text and returns the translation"""
        try:
            id = str(uuid.uuid4())
            
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Traduza o seguinte texto do {data['source_language']} para o {data['target_language']}: {data['text']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )

            self.gpt_database.translator(id, data['text'], response['choices'][0]['text'], data['user_id'])

            return response['choices'][0]['text']
        
        except Exception as err:
            return str(err)
    
    def writing_assistant(self, data):
        """This method receives the subject of a text and returns the text"""
        try:
            id = str(uuid.uuid4())

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Crie um texto para: {data['text']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )
            
            self.gpt_database.writing_assistant(id, data['text'], response['choices'][0]['text'], data['user_id'])

            return response['choices'][0]['text']
        
        except Exception as err:
            return str(err)