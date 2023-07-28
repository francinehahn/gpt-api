"""JWT - token"""
from flask_jwt_extended import create_access_token, get_jwt_identity

class Authentication:
    """Authentication class"""
    @staticmethod
    def generate_token(user_id):
        """Method that generates a token"""
        token = create_access_token(identity=user_id)
        return token

    @staticmethod
    def get_identity():
        """Method that verifies whether the token is valid"""
        user_id = get_jwt_identity()
        return user_id