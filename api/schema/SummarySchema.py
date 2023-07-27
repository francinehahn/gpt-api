from marshmallow import Schema, fields

class SummarySchema(Schema):
    user_id = fields.Str(required=True)
    text = fields.Str(required=True)