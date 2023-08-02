"""routes from /users"""
from flask import Blueprint
from flask_cors import cross_origin
from api.controllers.UserController import UserController
from api.services.UserService import UserService
from api.database.UserDatabase import UserDatabase
from api.externalServices.Authentication import Authentication
from api.externalServices.Criptography import Criptography

user_blueprint = Blueprint('users', __name__)

user_database = UserDatabase()
user_service = UserService(user_database, Authentication, Criptography)
user_controller = UserController(user_service)

@user_blueprint.route("/users/signup", methods=["POST"])
@cross_origin
def create_user():
    """Endpoint that receives a new user info and inserts it into the database"""
    return user_controller.create_user()

@user_blueprint.route("/users/login", methods=["POST"])
@cross_origin
def login():
    """Endpoint that receives the user info and returns a token"""
    return user_controller.login()