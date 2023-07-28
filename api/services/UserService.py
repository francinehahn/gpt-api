import uuid
from marshmallow import ValidationError
from api.schema.UserSchema import UserSchema
from api.schema.LoginSchema import LoginSchema
from api.schema.EmailSchema import EmailSchema
from api.errors.UserErrors import EmailAlreadyInUse, UserNotFound
from api.external_services.criptography import Criptography

class UserService:
    def __init__(self, user_database, authentication):
        self.user_database = user_database
        self.authentication = authentication

    def create_user(self, data):
        """This method receives user data from the controller and sends it to the database layer"""
        try:
            UserSchema().load(data)
            id = str(uuid.uuid4())

            #criptography
            hashed_password = Criptography.hash_password(data['password'])
            data['password'] = hashed_password

            self.user_database.create_user(id, data)
        
        except EmailAlreadyInUse as err:
            raise err
        except ValidationError as err:
            raise err
        except Exception as err:
            raise Exception(f"Unexpected error: {err}") from err
        
    def login(self, data):
        """This method receives user data from the controller and returns an auth token"""
        try:
            LoginSchema().load(data)
            user = self.user_database.get_user_by_email(data["email"])

            is_password_correct = Criptography.verify_password(data["password"], user[4])
            if (is_password_correct is False):
                raise UserNotFound("Incorrect login information.")

            token = self.authentication.generate_token(user[0])
            return token
        
        except EmailAlreadyInUse as err:
            raise err
        except UserNotFound as err:
            raise err
        except ValidationError as err:
            raise err
        except Exception as err:
            raise Exception(f"Unexpected error: {err}") from err
        
    def get_user_by_email(self, email):
        """This method receives an email from the controller and returns the user info"""
        try:
            print("email: ", email)
            EmailSchema().load({"email": email})
            response = self.user_database.get_user_by_email(email)
            return response
        
        except ValidationError as err:
            raise err
        except UserNotFound as err:
            raise err
        except Exception as err:
            raise Exception(f"Unexpected error: {err}") from err