from marshmallow import Schema, fields

class WritingAssistantSchema(Schema):
    text = fields.Str(required=True)