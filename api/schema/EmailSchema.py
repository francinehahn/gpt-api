from marshmallow import Schema, fields, validates, ValidationError
import re

class EmailSchema(Schema):
    email = fields.Email(required=True)
        
    @validates('email')
    def validate_email(self, email):
        email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValidationError('Invalid email.')