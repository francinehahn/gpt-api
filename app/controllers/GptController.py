from flask import jsonify, request
from marshmallow import ValidationError
from app.schema.RecipeSchema import RecipeSchema
from app.schema.SummarySchema import SummarySchema
from app.schema.TranslatorSchema import TranslatorSchema
from app.schema.WritingAssistantSchema import WritingAssistantSchema

class GptController:
    """This class receives data from the HTTP request and returns the response"""

    def __init__(self, gpt_service):
        self.gpt_service = gpt_service

    def create_recipe(self):
        """This method receives ingredients and sends it to the service layer"""
        try:
            data = RecipeSchema().load(request.json)

            response = self.gpt_service().create_recipe(data)
            
            response = jsonify(
                message = "Aqui está a receita:",
                data = response,
            )
            
            response.status_code = 201
            return response
        
        except ValidationError as err:
            response = jsonify(
                message = f"Validation error: {err}"
            )
            response.status_code = 400
            return response
        
        except Exception as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def create_summary(self):
        """This method receives a text and sends it to the service layer"""
        try:
            data = SummarySchema().load(request.json)
            response = self.gpt_service().create_summary(data)
            
            response = jsonify(
                message = "Aqui está o resumo do texto:",
                data = response
            )
            
            response.status_code = 201
            return response
        
        except ValidationError as err:
            response = jsonify(
                message = f"Validation error: {err}"
            )
            response.status_code = 400
            return response
        
        except Exception as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def translator(self):
        """This method receives a source language, a target language and a text and sends it to the service layer"""
        try:
            data = TranslatorSchema().load(request.json)
            response = self.gpt_service().translator(data)

            response = jsonify(
                message = "Aqui está a tradução que você pediu:",
                data = response
            )
            response.status_code = 201
            return response
    
        except ValidationError as err:
            response = jsonify(
                message = f"Validation error: {err}"
            )
            response.status_code = 400
            return response
        
        except Exception as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def writing_assistant(self):
        """This method receives a subject for a text and sends it to the service layer"""
        try:
            data = WritingAssistantSchema().load(request.json)
            response = self.gpt_service().writing_assistant(data)

            response = jsonify(
                message = "Aqui está o texto que você pediu:",
                data = response
            )
            response.status_code = 201
            return response
    
        except ValidationError as err:
            response = jsonify(
                message = f"Validation error: {err}"
            )
            response.status_code = 400
            return response
        
        except Exception as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        