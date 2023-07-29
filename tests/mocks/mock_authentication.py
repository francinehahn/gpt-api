"""JWT - token MOCK"""

class AuthenticationMock:
    """AuthenticationMock class"""
    @staticmethod
    def generate_token(user_id):
        """Method that generates a token"""
        return "token"

    @staticmethod
    def get_identity():
        """Method that verifies whether the token is valid"""
        return "8a85573b-2ea2-43a4-9c8d-91b959e6da3c"