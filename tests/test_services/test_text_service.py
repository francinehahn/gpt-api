"""Test Text Service"""
import pytest
from marshmallow import ValidationError
from api.errors.TextErrors import TextNotFound
from api.services.TextService import TextService
from tests.mocks.mock_text_database import MockTextDatabase
from tests.mocks.mock_openai import OpenAIMock
from tests.mocks.mock_authentication import AuthenticationMock

text_service = TextService(MockTextDatabase(), AuthenticationMock, OpenAIMock)

def test_create_text_method_when_input_is_correct():
    """This function tests the create text method in the service layer"""
    data = {'text': 'Benefícios da linhaça'}
    result = text_service.create_text(data)
    assert result is not None

def test_create_text_method_when_input_is_not_correct():
    """This function tests the create text method in the service layer"""
    data = ""
    with pytest.raises(ValidationError):
        text_service.create_text(data)

def test_get_texts_method():
    """This function tests the get texts method in the service layer"""
    result = text_service.get_texts()
    assert result is not None

def test_delete_text_by_id_when_text_id_exist():
    """This function tests the delete text by id method in the service layer"""
    text_id = "83e3fe01-a502-4328-8bee-fed6dc72616a"
    assert text_service.delete_text_by_id(text_id) is None

def test_delete_text_by_id_when_text_id_dont_exist():
    """This function tests the delete text by id method in the service layer"""
    text_id = "incorrect_id"
    with pytest.raises(TextNotFound):
        text_service.delete_text_by_id(text_id)

def test_regenerate_text():
    """This function tests the regenerate text method in the service layer"""
    assert text_service.regenerate_text() is None