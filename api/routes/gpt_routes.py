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

@gpt_blueprint.route("/summary", methods=["POST"])
@jwt_required()
def create_summary():
    """Endpoint that receives this body {"text": "História do titanic"} and return a summary"""
    return gpt_controller.create_summary()

@gpt_blueprint.route("/translator", methods=["POST"])
@jwt_required()
def translator():
    """Endpoint that receives a source_language, a target_language and a text to be translated"""
    return gpt_controller.translator()

@gpt_blueprint.route("/writing-assistant", methods=["POST"])
@jwt_required()
def writing_assistant():
    """Endpoint that receives a subject and returns a text that addresses the subject"""
    return gpt_controller.writing_assistant()