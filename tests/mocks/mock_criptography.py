"Criptography Mock"
class CriptographyMock:
    @staticmethod
    def hash_password(password):
        return "hashed_password"
    
    @staticmethod
    def verify_password(password, hashed_password):
        if password == "12345678":
            return True
        else:
            return False