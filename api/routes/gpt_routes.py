"""routes from the gpt api"""
from flask import Blueprint
from api.controllers.GptController import GptController
from api.services.GptService import GptService


gpt_blueprint = Blueprint('gpt', __name__)
gpt_controller = GptController(GptService)

@gpt_blueprint.route("/create-recipe", methods=["POST"])
#@jwt_required()
def create_recipe():
    """Endpoint that receives ingredients and returns a recipe"""
    return gpt_controller.create_recipe()

@gpt_blueprint.route("/summary", methods=["POST"])
#@jwt_required()
def create_summary():
    """Endpoint that receives this body {"text": "História do titanic"} and return a summary"""
    return gpt_controller.create_summary()

@gpt_blueprint.route("/translator", methods=["POST"])
#@jwt_required()
def translator():
    """Endpoint that receives a source_language, a target_language and a text to be translated"""
    return gpt_controller.translator()

@gpt_blueprint.route("/writing-assistant", methods=["POST"])
#@jwt_required()
def writing_assistant():
    """Endpoint that receives a subject and returns a text that addresses the subject"""
    return gpt_controller.writing_assistant()