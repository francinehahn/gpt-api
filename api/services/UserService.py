import uuid
from api.database.UserDatabase import UserDatabase
from api.schema.UserSchema import UserSchema
from api.errors.UserErrors import EmailAlreadyInUse

class UserService:
    def __init__(self):
        self.user_database = UserDatabase()

    def create_user(self, data):
        """This method receives user data from the controller and sends it to the database layer"""
        try:
            UserSchema().load(data)

            #Validar se email já não está no banco de dados

            id = str(uuid.uuid4())
            self.user_database.create_user(id, data)
        
        except EmailAlreadyInUse as err:
            raise err
        except Exception as err:
            raise Exception(f"Unexpected error: {err}") from err