"""Text controller"""
from marshmallow import ValidationError
from mysql.connector import Error
from flask import jsonify, request
from api.errors.TextErrors import TextNotFound

class TextController:
    """This class receives data from the HTTP request and returns the response"""

    def __init__(self, text_service):
        self.text_service = text_service

    def create_text(self):
        """This method receives a subject and returns a text"""
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
    
    def get_texts(self):
        """This method receives a token and returns all the texts registered in the user account"""
        try:
            response = self.text_service.get_texts()
            
            response = jsonify(
                texts = response
            )
            
            response.status_code = 200
            return response
        
        except Error as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def delete_text_by_id(self, text_id):
        """This method receives a token and a text_id and returns a message in case of success"""
        try:
            response = self.text_service.delete_text_by_id(text_id)
            response = jsonify(
                message = "The text has been deleted successfully."
            )
            
            response.status_code = 200
            return response
        
        except TextNotFound as err:
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