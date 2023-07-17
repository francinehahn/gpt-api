import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class GptService:

    def create_recipe(self, data):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Crie uma receita com os seguintes ingredientes: {data['ingredients']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )
            return response['choices'][0]['text']
        
        except Exception as e:
            return str(e)
    
    def create_summary(self, data):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Resuma o seguinte texto: {data['text']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )
            return response['choices'][0]['text']
        
        except Exception as e:
            return str(e)
        
    def translator(self, data):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Traduza o seguinte texto do {data['source_language']} para o {data['target_language']}: {data['text']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )
            return response['choices'][0]['text']
        
        except Exception as e:
            return str(e)
    
    def writing_assistant(self, data):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Crie um texto para: {data['text']}",
                temperature=0.8,
                max_tokens=2048,
                n=1,
                stop=None
            )
            return response['choices'][0]['text']
        
        except Exception as e:
            return str(e)