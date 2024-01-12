"""OpenAI"""
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAI:
    """This class contains methods that generate resposnes from the openAI api"""
    @staticmethod
    def generate_recipe(question):
        """This method returns a recipe"""
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Crie uma receita com os seguintes ingredientes: {question}",
            temperature=0.8,
            max_tokens=2048,
            n=1,
            stop=None
        )
        return response['choices'][0]['text']
    
    @staticmethod
    def generate_summary(question):
        """This method returns a summary"""
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Resuma o seguinte texto: {question}",
            temperature=0.8,
            max_tokens=2048,
            n=1,
            stop=None
        )
        return response['choices'][0]['text']
    
    @staticmethod
    def generate_text(question):
        """This method returns a text"""
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Crie um texto para: {question}",
            temperature=0.8,
            max_tokens=2048,
            n=1,
            stop=None
        )
        return response['choices'][0]['text']
    
    @staticmethod
    def generate_translation(question):
        """This method returns a translation"""
        print('TRANSLATION')
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Traduza o seguinte texto do {question['source_language']} para o {question['target_language']}: {question['text']}",
            temperature=0.8,
            max_tokens=2048,
            n=1,
            stop=None
        )
        return response['choices'][0]['text']
  