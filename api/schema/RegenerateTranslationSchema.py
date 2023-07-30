"""RegenerateTranslationSchema"""
from marshmallow import Schema, fields

class RegenerateTranslationSchema(Schema):
    """Validation of the regenerate translator input"""
    source_language = fields.Str(required=True)
    target_language = fields.Str(required=True)
    