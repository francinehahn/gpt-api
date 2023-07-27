from marshmallow import Schema, fields

class RecipeSchema(Schema):
    user_id = fields.Str(required=True)
    ingredients = fields.Str(required=True)