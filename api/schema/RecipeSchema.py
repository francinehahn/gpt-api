"""Recipe schema"""
from marshmallow import Schema, fields

class RecipeSchema(Schema):
    """Validation of the create recipe input"""
    ingredients = fields.Str(required=True)
    