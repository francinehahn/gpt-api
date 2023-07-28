"""Summary schema"""
from marshmallow import Schema, fields

class SummarySchema(Schema):
    """Validation of the create a summary input"""
    text = fields.Str(required=True)