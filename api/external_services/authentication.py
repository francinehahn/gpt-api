"""JWT - token"""
from flask_jwt_extended import create_access_token, get_jwt_identity

class Authentication:
    @staticmethod
    def generate_token(id):
        token = create_access_token(identity=id)
        return token

    @staticmethod
    def get_identity():
        user_id = get_jwt_identity()
        return user_id