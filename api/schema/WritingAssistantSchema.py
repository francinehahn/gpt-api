"""Writing assistant schema"""
from marshmallow import Schema, fields

class WritingAssistantSchema(Schema):
    """Required field"""
    text = fields.Str(required=True)
    