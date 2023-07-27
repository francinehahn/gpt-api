from marshmallow import Schema, fields

class UserSchema(Schema):
    user_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)