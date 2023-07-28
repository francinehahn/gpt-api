"""Gpt controller layer"""
from marshmallow import ValidationError
from mysql.connector import Error
from flask import jsonify, request

class GptController:
    """This class receives data from the HTTP request and returns the response"""

    def __init__(self, gpt_service):
        self.gpt_service = gpt_service

    def create_recipe(self):
        """This method receives ingredients and sends it to the service layer"""
        try:
            data = request.json
            response = self.gpt_service.create_recipe(data)
            
            response = jsonify(
                message = "The recipe has been registered successfully",
                data = response
            )
            
            response.status_code = 201
            return response
        
        except ValidationError as err:
            response = jsonify(
                message = f"Validation error: {err}"
            )
            response.status_code = 422
            return response
        
        except Error as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def get_recipes(self):
        """This method receives a token and sends it to the service layer"""
        try:
            response = self.gpt_service.get_recipes()
            
            response = jsonify(
                recipes = response
            )
            
            response.status_code = 200
            return response
        
        except Error as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def create_summary(self):
        """This method receives a text and sends it to the service layer"""
        try:
            data = request.json
            response = self.gpt_service.create_summary(data)
            
            response = jsonify(
                message = "The summary has been registered successfully",
                data = response
            )
            
            response.status_code = 201
            return response
        
        except ValidationError as err:
            response = jsonify(
                message = f"Validation error: {err}"
            )
            response.status_code = 422
            return response
        
        except Error as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def create_translation(self):
        """This method receives a source language, a target language and a text and sends it to the service layer"""
        try:
            data = request.json
            response = self.gpt_service.create_translation(data)

            response = jsonify(
                message = "The translation has been registered successfully",
                data = response
            )
            response.status_code = 201
            return response
    
        except ValidationError as err:
            response = jsonify(
                message = f"Validation error: {err}"
            )
            response.status_code = 422
            return response
    
        except Error as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def create_text(self):
        """This method receives a subject for a text and sends it to the service layer"""
        try:
            data = request.json
            response = self.gpt_service.create_text(data)

            response = jsonify(
                message = "The text has been registered successfully",
                data = response
            )
            response.status_code = 201
            return response
    
        except ValidationError as err:
            response = jsonify(
                message = f"Validation error: {err}"
            )
            response.status_code = 422
            return response

        except Error as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        