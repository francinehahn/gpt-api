from marshmallow import Schema, fields

class TranslatorSchema(Schema):
    user_id = fields.Str(required=True)
    source_language = fields.Str(required=True)
    target_language = fields.Str(required=True)
    text = fields.Str(required=True)