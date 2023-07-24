from marshmallow import Schema, fields

class RecipeSchema(Schema):
    ingredients = fields.Str(required=True)