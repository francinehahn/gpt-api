"""User schema"""
from marshmallow import Schema, fields, validates, ValidationError
import re

class UserSchema(Schema):
    """Validation of the create user input"""
    user_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    password = fields.Str(required=True)
        
    @validates('user_name')
    def validate_user_name(self, user_name):
        """Validation of the user name"""
        if len(user_name) < 6:
            raise ValidationError('The user name mus have at least 6 characters.')

        if ' ' not in user_name:
            raise ValidationError('Provide the full name.')
    
    @validates('email')
    def validate_email(self, email):
        """Validation of the email"""
        email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValidationError('Invalid email.')
        
    @validates('phone')
    def validate_phone(self, phone):
        """Validation of the phone number"""
        if len(phone) != 11:
            raise ValidationError('The phone number must have 11 digits.')

        if not phone.isdigit():
            raise ValidationError('The phone number must contain only numbers.')
        
    @validates('password')
    def validate_password(self, password):
        """Validation of the password"""
        if len(password) < 8:
            raise ValidationError('The password must have at least 8 characters.')