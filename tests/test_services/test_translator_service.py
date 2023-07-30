"""Test Translator Service"""
import pytest
from marshmallow import ValidationError
from api.errors.TranslatorErrors import TranslationNotFound
from api.services.TranslatorService import TranslatorService
from tests.mocks.mock_translator_database import TranslatorDatabaseMock
from tests.mocks.mock_openai import OpenAIMock
from tests.mocks.mock_authentication import AuthenticationMock

translator_service = TranslatorService(TranslatorDatabaseMock(), AuthenticationMock, OpenAIMock)

def test_create_translation_method_when_input_is_correct():
    """This function tests the create translation method in the service layer"""
    data = {
        "source_language": "português",
        "target_language": "inglês",
        "text": "Tradução teste que deve ser apagada"
    }
    result = translator_service.create_translation(data)
    assert result is not None

def test_create_translation_method_when_input_is_not_correct():
    """This function tests the create translation method in the service layer"""
    data = ""
    with pytest.raises(ValidationError):
        translator_service.create_translation(data)

def test_create_translation_method_when_input_is_not_correct_2():
    """This function tests the create translation method in the service layer"""
    data = {
        "source_language": 2,
        "target_language": "inglês",
        "text": "Tradução teste que deve ser apagada"
    }
    with pytest.raises(ValidationError):
        translator_service.create_translation(data)

def test_get_translations_method():
    """This function tests the get translations method in the service layer"""
    result = translator_service.get_translations()
    assert result is not None

def test_delete_translation_by_id_when_translation_id_exist():
    """This function tests the delete translation by id method in the service layer"""
    translation_id = "83e3fe01-a502-4328-8bee-fed6dc72616a"
    assert translator_service.delete_translation_by_id(translation_id) is None

def test_delete_translation_by_id_when_translation_id_dont_exist():
    """This function tests the delete translation by id method in the service layer"""
    translation_id = "incorrect_id"
    with pytest.raises(TranslationNotFound):
        translator_service.delete_translation_by_id(translation_id)

def test_regenerate_translation_when_input_is_correct():
    """This function tests the regenerate translation method in the service layer"""
    data = {
        "source_language": "português",
        "target_language": "árabe"
    }
    assert translator_service.regenerate_translation(data) is None

def test_regenerate_translation_when_input_is_incorrect():
    """This function tests the regenerate translation method in the service layer"""
    data = {
        "source_language": 2,
        "target_language": "árabe"
    }
    with pytest.raises(ValidationError):
        translator_service.regenerate_translation(data)