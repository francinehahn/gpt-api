from marshmallow import Schema, fields, validates, ValidationError
import re

class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
        
    @validates('email')
    def validate_email(self, email):
        email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValidationError('Invalid email.')
            
    @validates('password')
    def validate_password(self, password):
        if len(password) < 8:
            raise ValidationError('The password must have at least 8 characters.')