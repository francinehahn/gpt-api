"""TranslatorRoutes"""
from flask_jwt_extended import jwt_required
from flask import Blueprint
from api.controllers.TranslatorController import TranslatorController
from api.services.TranslatorService import TranslatorService
from api.database.TranslatorDatabase import TranslatorDatabase
from api.externalServices.Authentication import Authentication

translator_blueprint = Blueprint('translator', __name__)

translator_database = TranslatorDatabase()
translator_service = TranslatorService(translator_database, Authentication)
translator_controller = TranslatorController(translator_service)

@translator_blueprint.route("/create-translation", methods=["POST"])
@jwt_required()
def create_translation():
    """Endpoint that receives a source_language, a target_language and a text to be translated"""
    return translator_controller.create_translation()

@translator_blueprint.route("/get-translations", methods=["GET"])
@jwt_required()
def get_translations():
    """Endpoint that receives a token and returns the translations from the user"""
    return translator_controller.get_translations()