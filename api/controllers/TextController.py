"""Text controller"""
from marshmallow import ValidationError
from mysql.connector import Error
from flask import jsonify, request

class TextController:
    """This class receives data from the HTTP request and returns the response"""

    def __init__(self, text_service):
        self.text_service = text_service

    def create_text(self):
        """This method receives a subject for a text and sends it to the service layer"""
        try:
            data = request.json
            response = self.text_service.create_text(data)

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
    
    def get_texts(self):
        """This method receives a token and sends it to the service layer"""
        try:
            response = self.text_service.get_texts()
            
            response = jsonify(
                texts = response
            )
            
            response.status_code = 200
            return response
        
        except Error as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response