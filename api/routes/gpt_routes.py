"""routes from the gpt api"""
from flask_jwt_extended import jwt_required
from flask import Blueprint
from api.controllers.GptController import GptController
from api.services.GptService import GptService
from api.database.GptDatabase import GptDatabase
from api.external_services.authentication import Authentication

gpt_blueprint = Blueprint('gpt', __name__)

gpt_database = GptDatabase()
gpt_service = GptService(gpt_database, Authentication)
gpt_controller = GptController(gpt_service)

@gpt_blueprint.route("/create-recipe", methods=["POST"])
@jwt_required()
def create_recipe():
    """Endpoint that receives ingredients and returns a recipe"""
    return gpt_controller.create_recipe()

@gpt_blueprint.route("/create-summary", methods=["POST"])
@jwt_required()
def create_summary():
    """Endpoint that receives this body {"text": "História do titanic"} and return a summary"""
    return gpt_controller.create_summary()

@gpt_blueprint.route("/create-translation", methods=["POST"])
@jwt_required()
def translator():
    """Endpoint that receives a source_language, a target_language and a text to be translated"""
    return gpt_controller.create_translation()

@gpt_blueprint.route("/create-text", methods=["POST"])
@jwt_required()
def create_text():
    """Endpoint that receives a subject and returns a text that addresses the subject"""
    return gpt_controller.create_text()

@gpt_blueprint.route("/get-recipes", methods=["GET"])
@jwt_required()
def get_recipes():
    """Endpoint that receives a token and returns the recipes from the user"""
    return gpt_controller.get_recipes()

@gpt_blueprint.route("/get-summaries", methods=["GET"])
@jwt_required()
def get_summaries():
    """Endpoint that receives a token and returns the summaries from the user"""
    return gpt_controller.get_summaries()

@gpt_blueprint.route("/get-translations", methods=["GET"])
@jwt_required()
def get_translations():
    """Endpoint that receives a token and returns the translations from the user"""
    return gpt_controller.get_translations()

@gpt_blueprint.route("/get-texts", methods=["GET"])
@jwt_required()
def get_texts():
    """Endpoint that receives a token and returns the texts from the user"""
    return gpt_controller.get_texts()