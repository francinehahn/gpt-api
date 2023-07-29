"""Translator controller"""
from marshmallow import ValidationError
from mysql.connector import Error
from flask import jsonify, request
from api.errors.TranslatorErrors import TranslationNotFound

class TranslatorController:
    """This class receives data from the HTTP request and returns the response"""

    def __init__(self, translator_service):
        self.translator_service = translator_service
         
    def create_translation(self):
        """This method receives a source language, a target language and a text and returns the translation"""
        try:
            data = request.json
            response = self.translator_service.create_translation(data)

            response = jsonify(
                message = "The translation has been registered successfully",
                data = response
            )
            response.status_code = 201
            return response
    
        except ValidationError as err:
            response = jsonify(
                error = f"Validation error: {err}"
            )
            response.status_code = 422
            return response
    
        except Error as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response

    def get_translations(self):
        """This method receives a token and returns all the translations registered in the user account"""
        try:
            response = self.translator_service.get_translations()
            
            response = jsonify(
                translations = response
            )
            
            response.status_code = 200
            return response
        
        except Error as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def delete_translation_by_id(self, translation_id):
        """This method receives a token and a translation_id and returns a message in case of success"""
        try:
            response = self.translator_service.delete_translation_by_id(translation_id)
            response = jsonify(
                message = "The translation has been deleted successfully."
            )
            
            response.status_code = 200
            return response
        
        except TranslationNotFound as err:
            response = jsonify(
                error = str(err)
            )
            response.status_code = 404
            return response
        
        except Error as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response