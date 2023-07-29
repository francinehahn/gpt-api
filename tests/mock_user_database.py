"""Mock User Database"""

class MockUserDatabase:
    """This is a mock of the user database layer"""
    def create_user(self, user_id, data):
        """This method receives the user info from the service layer and inserts it into the database"""

    def get_user_by_email(self, email):
        return ('8a85573b-2ea2-43a4-9c8d-91b959e6da3c', 'Lucas Viana', 'lucas_viana@hotmail.com', '51982521177', '$2b$12$SGLKYbG8wVFfFjr.9ukrNupq3T/BAlKMWQa7rp0JZUpY1QcUKunX2')