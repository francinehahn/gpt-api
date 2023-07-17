from marshmallow import Schema, fields

class SummarySchema(Schema):
    text = fields.Str(required=True)