"""RecipeRoutes"""
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from flask import Blueprint
from api.controllers.RecipeController import RecipeController
from api.services.RecipeService import RecipeService
from api.database.RecipeDatabase import RecipeDatabase
from api.externalServices.Authentication import Authentication
from api.externalServices.OpenAi import OpenAI

recipe_blueprint = Blueprint('recipe', __name__)

recipe_database = RecipeDatabase()
recipe_service = RecipeService(recipe_database, Authentication, OpenAI)
recipe_controller = RecipeController(recipe_service)

@recipe_blueprint.route("/create-recipe", methods=["POST"])
@cross_origin
@jwt_required()
def create_recipe():
    """Endpoint that receives ingredients and returns a recipe"""
    return recipe_controller.create_recipe()

@recipe_blueprint.route("/get-recipes", methods=["GET"])
@cross_origin
@jwt_required()
def get_recipes():
    """Endpoint that receives a token and returns the recipes from the user"""
    return recipe_controller.get_recipes()

@recipe_blueprint.route("/delete-recipe/<string:recipe_id>", methods=["DELETE"])
@cross_origin
@jwt_required()
def delete_recipe_by_id(recipe_id):
    """Endpoint that receives a token and a recipe_id and deletes the recipe"""
    return recipe_controller.delete_recipe_by_id(recipe_id)

@recipe_blueprint.route("/regenerate-recipe", methods=["PATCH"])
@cross_origin
@jwt_required()
def regenerate_recipe():
    """Endpoint that receives a token and updates the recipe"""
    return recipe_controller.regenerate_recipe()