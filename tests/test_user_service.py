"""Test Translator Service"""
import pytest
from marshmallow import ValidationError
from api.errors.UserErrors import IncorrectLoginInfo
from api.services.UserService import UserService
from tests.mocks.mock_user_database import MockUserDatabase
from tests.mocks.mock_authentication import AuthenticationMock
from tests.mocks.mock_criptography import CriptographyMock

user_service = UserService(MockUserDatabase(), AuthenticationMock, CriptographyMock)

def test_create_user_method_when_input_is_correct():
    """This function tests the create user method in the service layer"""
    data = {
        "user_name": "Lucas Viana",
        "email": "lucas_viana@hotmail.com",
        "phone": "51982521177",
        "password": "12345678"
    }
    user_service.create_user(data)

def test_create_user_method_when_input_is_incorrect():
    """This function tests the create user method in the service layer"""
    data = {
        "user_name": "Lucas Viana",
        "email": "lucas_viana@hotmail.com",
        "phone": 51982521177,
        "password": "12345678"
    }
    with pytest.raises(ValidationError):
        user_service.create_user(data)

def test_login_method_when_input_is_correct():
    """This function tests the login method in the service layer"""
    data = {
        "email": "lucas_viana@hotmail.com",
        "password": "12345678"
    }
    result = user_service.login(data)
    assert result == "token"

def test_login_method_when_password_is_incorrect():
    """This function tests the login method in the service layer"""
    data = {
        "email": "lucas_viana@hotmail.com",
        "password": "12345678910"
    }
    with pytest.raises(IncorrectLoginInfo):
        user_service.login(data)
  
def test_login_method_when_email_is_incorrect():
    """This function tests the login method in the service layer"""
    data = {
        "email": "incorrect_email@gmail.com",
        "password": "12345678"
    }
    with pytest.raises(IncorrectLoginInfo):
        user_service.login(data)

def test_login_method_when_input_is_incorrect():
    """This function tests the login method in the service layer"""
    data = {
        "email": "lucas_viana@hotmail.com",
        "password": 12345678
    }
    with pytest.raises(ValidationError):
        user_service.login(data)