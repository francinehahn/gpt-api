"""UserService.py"""
import uuid
from marshmallow import ValidationError
from mysql.connector import Error

from api.schema.UserSchema import UserSchema
from api.schema.LoginSchema import LoginSchema
from api.errors.UserErrors import EmailAlreadyInUse, IncorrectLoginInfo

class UserService:
    """Service layer"""
    def __init__(self, user_database, authentication, criptography):
        self.user_database = user_database
        self.authentication = authentication
        self.criptography = criptography

    def create_user(self, data):
        """This method receives user data from the controller and sends it to the database layer"""
        try:
            UserSchema().load(data)
            user_id = str(uuid.uuid4())

            #criptography
            hashed_password = self.criptography.hash_password(data['password'])
            data['password'] = hashed_password

            self.user_database.create_user(user_id, data)
        
        except EmailAlreadyInUse as err:
            raise err
        except ValidationError as err:
            raise err
        except Error as err:
            raise err
        
    def login(self, data):
        """This method receives user data from the controller and returns an auth token"""
        try:
            LoginSchema().load(data)
            user = self.user_database.get_user_by_email(data["email"])

            is_password_correct = self.criptography.verify_password(data["password"], user[4])
            if (is_password_correct is False):
                raise IncorrectLoginInfo("Email or password are incorrect.")

            token = self.authentication.generate_token(user[0])
            return token
        
        except EmailAlreadyInUse as err:
            raise err
        except IncorrectLoginInfo as err:
            raise err
        except ValidationError as err:
            raise err
        except Error as err:
            raise err