"""Translator schema"""
from marshmallow import Schema, fields

class TranslatorSchema(Schema):
    """Validation of the translator input"""
    source_language = fields.Str(required=True)
    target_language = fields.Str(required=True)
    text = fields.Str(required=True)