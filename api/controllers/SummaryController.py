"""Summary controller"""
from marshmallow import ValidationError
from botocore.exceptions import ClientError
from flask import jsonify, request
from api.errors.SummaryErrors import SummaryNotFound
from api.errors.SummaryErrors import NoSummariesToUpdate

class SummaryController:
    """This class receives data from the HTTP request and returns the response"""
    def __init__(self, summary_service):
        self.summary_service = summary_service
    
    def create_summary(self):
        """This method receives a text and returns a summary of it"""
        try:
            data = request.json
            response = self.summary_service.create_summary(data)
            response = jsonify(
                message = "The summary has been registered successfully",
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

    def get_summaries(self):
        """This method receives a token and returns all the summaryes registered in the user account"""
        try:
            response = self.summary_service.get_summaries()
            response = jsonify(
                summaries = response
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
        
    def delete_summary_by_id(self, summary_id):
        """This method receives a token and a summary_id and returns a message in case of success"""
        try:
            response = self.summary_service.delete_summary_by_id(summary_id)
            response = jsonify(
                message = "The summary has been deleted successfully."
            )
            response.status_code = 200
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except SummaryNotFound as err:
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
        
    def regenerate_summary(self):
        """This method receives a token and returns a message in case of success"""
        try:
            response = self.summary_service.regenerate_summary()
            response = jsonify(
                message = "The summary has been updated successfully."
            )
            response.status_code = 200
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except NoSummariesToUpdate as err:
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
        