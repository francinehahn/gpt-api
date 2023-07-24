from marshmallow import Schema, fields

class TranslatorSchema(Schema):
    source_language = fields.Str(required=True)
    target_language = fields.Str(required=True)
    text = fields.Str(required=True)