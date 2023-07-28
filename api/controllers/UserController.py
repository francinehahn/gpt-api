"""User controller layer"""
from flask import jsonify, request
from marshmallow import ValidationError
from mysql.connector import Error
from api.errors.UserErrors import EmailAlreadyInUse, IncorrectLoginInfo

class UserController:
    """Controller layer"""
    def __init__(self, user_service):
        self.user_service = user_service

    def create_user(self):
        """This method receives data from a new user and sends it to the service layer"""
        try:
            data = request.json
            self.user_service.create_user(data)
            
            response = jsonify(
                message = "The user has been registered successfully"
            )
            
            response.status_code = 201
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
        
        except Error as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
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
        
        except Error as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response