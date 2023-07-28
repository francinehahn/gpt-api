"""User controller layer"""
from flask import jsonify, request
from marshmallow import ValidationError
from api.errors.UserErrors import EmailAlreadyInUse, UserNotFound

class UserController:

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
            response.status_code = 400
            return response
        
        except EmailAlreadyInUse as err:
            response = jsonify(
                error = str(err)
            )
            response.status_code = 400
            return response
        
        except Exception as err:
            response = jsonify(error = str(err))
            response.status_code = 500
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
            response.status_code = 400
            return response
        
        except UserNotFound as err:
            response = jsonify(
                error = str(err)
            )
            response.status_code = 404
            return response
        
        except Exception as err:
            response = jsonify(error = str(err))
            response.status_code = 500
            return response
        
    def get_user_by_email(self, email):
        """This method receives an email and returns the user information"""
        try:
            email = request.view_args['email']
            data = self.user_service.get_user_by_email(email)
            response = {
                "user_id": data[0],
                "user_name": data[1],
                "email": data[2],
                "phone": data[3],
                "password": data[4]
            }

            response = jsonify(
                data = response
            )
            
            response.status_code = 200
            return response
        
        except ValidationError as err:
            response = jsonify(
                error = f"Validation error: {str(err)}"
            )
            response.status_code = 400
            return response
        
        except UserNotFound as err:
            response = jsonify(
                error = str(err)
            )
            response.status_code = 404
            return response
        
        except Exception as err:
            response = jsonify(error = str(err))
            response.status_code = 500
            return response
        