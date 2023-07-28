"""SummaryRoutes"""
from flask_jwt_extended import jwt_required
from flask import Blueprint
from api.controllers.SummaryController import SummaryController
from api.services.SummaryService import SummaryService
from api.database.SummaryDatabase import SummaryDatabase
from api.externalServices.Authentication import Authentication

summary_blueprint = Blueprint('summary', __name__)

summary_database = SummaryDatabase()
summary_service = SummaryService(summary_database, Authentication)
summary_controller = SummaryController(summary_service)

@summary_blueprint.route("/create-summary", methods=["POST"])
@jwt_required()
def create_summary():
    """Endpoint that receives this body {"text": "História do titanic"} and return a summary"""
    return summary_controller.create_summary()

@summary_blueprint.route("/get-summaries", methods=["GET"])
@jwt_required()
def get_summaries():
    """Endpoint that receives a token and returns the summaries from the user"""
    return summary_controller.get_summaries()

@summary_blueprint.route("/delete-summary/<string:summary_id>", methods=["DELETE"])
@jwt_required()
def delete_summary_by_id(summary_id):
    """Endpoint that receives a token and a recipe_id and deletes the recipe from the user"""
    return summary_controller.delete_summary_by_id(summary_id)