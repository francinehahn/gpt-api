"""TextRoutes"""
from flask_jwt_extended import jwt_required
from flask import Blueprint
from api.controllers.TextController import TextController
from api.services.TextService import TextService
from api.database.TextDatabase import TextDatabase
from api.externalServices.Authentication import Authentication

text_blueprint = Blueprint('text', __name__)

text_database = TextDatabase()
text_service = TextService(text_database, Authentication)
text_controller = TextController(text_service)

@text_blueprint.route("/create-text", methods=["POST"])
@jwt_required()
def create_text():
    """Endpoint that receives a subject and returns a text that addresses the subject"""
    return text_controller.create_text()

@text_blueprint.route("/get-texts", methods=["GET"])
@jwt_required()
def get_texts():
    """Endpoint that receives a token and returns the texts from the user"""
    return text_controller.get_texts()

@text_blueprint.route("/delete-text/<string:text_id>", methods=["DELETE"])
@jwt_required()
def delete_text_by_id(text_id):
    """Endpoint that receives a token and a text_id and deletes the text"""
    return text_controller.delete_text_by_id(text_id)