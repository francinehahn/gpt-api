"""User controller"""
from flask import jsonify, request
from marshmallow import ValidationError
from botocore.exceptions import ClientError
from api.errors.UserErrors import EmailAlreadyInUse, IncorrectLoginInfo

class UserController:
    """Controller layer"""
    def __init__(self, user_service):
        self.user_service = user_service

    def create_user(self):
        """This method receives data from a new user and returns a message in case of success"""
        try:
            data = request.json
            self.user_service.create_user(data)
            response = jsonify(
                message = "The user has been registered successfully."
            )
            response.status_code = 201
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except ValidationError as err:
            response = jsonify(
                error = f"Validation error: {str(err)}"
            )
            response.status_code = 422
            return response
        except EmailAlreadyInUse as err:
            response = jsonify(
                error = str(err)
            )
            response.status_code = 409
            return response
        except ClientError as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def login(self):
        """This method receives data from a user and returns an auth token"""
        try:
            data = request.json
            token = self.user_service.login(data)
            response = jsonify(
                token = token
            )
            response.status_code = 200
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except ValidationError as err:
            response = jsonify(
                error = f"Validation error: {str(err)}"
            )
            response.status_code = 422
            return response
        except IncorrectLoginInfo as err:
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
        