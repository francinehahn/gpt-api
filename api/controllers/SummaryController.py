"""Summary controller"""
from marshmallow import ValidationError
from mysql.connector import Error
from flask import jsonify, request
from api.errors.SummaryErrors import SummaryNotFound

class SummaryController:
    """This class receives data from the HTTP request and returns the response"""

    def __init__(self, summary_service):
        self.summary_service = summary_service
    
    def create_summary(self):
        """This method receives a text and sends it to the service layer"""
        try:
            data = request.json
            response = self.summary_service.create_summary(data)
            
            response = jsonify(
                message = "The summary has been registered successfully",
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

    def get_summaries(self):
        """This method receives a token and sends it to the service layer"""
        try:
            response = self.summary_service.get_summaries()
            
            response = jsonify(
                summaries = response
            )
            
            response.status_code = 200
            return response
        
        except Error as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def delete_summary_by_id(self, summary_id):
        """This method receives a token and a summary_id and sends them to the service layer"""
        try:
            response = self.summary_service.delete_summary_by_id(summary_id)
            response = jsonify(
                message = "The summary has been deleted successfully."
            )
            
            response.status_code = 200
            return response
        
        except SummaryNotFound as err:
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