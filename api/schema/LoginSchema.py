"""Login schema"""
import re
from marshmallow import Schema, fields, validates, ValidationError

class LoginSchema(Schema):
    """Validation of the login input"""
    email = fields.Str(required=True)
    password = fields.Str(required=True)
        
    @validates('email')
    def validate_email(self, email):
        """Email validation"""
        email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValidationError('Invalid email.')
            
    @validates('password')
    def validate_password(self, password):
        """Password validation"""
        if len(password) < 8:
            raise ValidationError('The password must have at least 8 characters.')
        