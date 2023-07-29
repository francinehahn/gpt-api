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
            engine="text-davinci-003",
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
            engine="text-davinci-003",
            prompt=f"Resuma o seguinte texto: {question}",
            temperature=0.8,
            max_tokens=2048,
            n=1,
            stop=None
        )
        return response['choices'][0]['text']