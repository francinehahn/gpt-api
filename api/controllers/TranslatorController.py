"""Translator controller"""
from marshmallow import ValidationError
from botocore.exceptions import ClientError
from flask import jsonify, request
from api.errors.TranslatorErrors import TranslationNotFound
from api.errors.TranslatorErrors import NoTranslationsToUpdate

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
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except ValidationError as err:
            response = jsonify(
                error = f"Validation error: {err}"
            )
            response.status_code = 422
            return response
        except ClientError as err:
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
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except ClientError as err:
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
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except TranslationNotFound as err:
            response = jsonify(
                error = str(err)
            )
            response.status_code = 404
            return response
        except ClientError as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def regenerate_translation(self):
        """This method receives a token and returns a message in case of success"""
        try:
            data = request.json
            response = self.translator_service.regenerate_translation(data)
            response = jsonify(
                message = "The translation has been updated successfully."
            )
            response.status_code = 200
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except ValidationError as err:
            response = jsonify(
                error = f"Validation error: {err}"
            )
            response.status_code = 422
            return response
        except NoTranslationsToUpdate as err:
            response = jsonify(
                error = str(err)
            )
            response.status_code = 422
            return response
        except ClientError as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        