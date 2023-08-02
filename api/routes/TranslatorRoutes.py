"""TranslatorRoutes"""
from flask_jwt_extended import jwt_required
from flask import Blueprint
from api.controllers.TranslatorController import TranslatorController
from api.services.TranslatorService import TranslatorService
from api.database.TranslatorDatabase import TranslatorDatabase
from api.externalServices.Authentication import Authentication
from api.externalServices.OpenAi import OpenAI

translator_blueprint = Blueprint('translator', __name__)

translator_database = TranslatorDatabase()
translator_service = TranslatorService(translator_database, Authentication, OpenAI)
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

@translator_blueprint.route("/delete-translation/<string:translation_id>", methods=["DELETE"])
@jwt_required()
def delete_translation_by_id(translation_id):
    """Endpoint that receives a token and a translation_id and deletes the translation"""
    return translator_controller.delete_translation_by_id(translation_id)

@translator_blueprint.route("/regenerate-translation", methods=["PATCH"])
@jwt_required()
def regenerate_translation():
    """Endpoint that receives a token and updates the translation"""
    return translator_controller.regenerate_translation()