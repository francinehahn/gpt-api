"""Test Recipe Service"""
import pytest
from marshmallow import ValidationError
from api.errors.RecipeErrors import RecipeNotFound
from api.services.RecipeService import RecipeService
from tests.mocks.mock_recipe_database import RecipeDatabaseMock
from tests.mocks.mock_openai import OpenAIMock
from tests.mocks.mock_authentication import AuthenticationMock

recipe_service = RecipeService(RecipeDatabaseMock(), AuthenticationMock, OpenAIMock)

def test_create_recipe_method_when_input_is_correct():
    """This function tests the create recipe method in the service layer"""
    data = {'ingredients': 'arroz, creme de leite, leite condensado, leite, canela, essência de baunilha'}
    result = recipe_service.create_recipe(data)
    assert result is not None

def test_create_recipe_method_when_input_is_not_correct():
    """This function tests the create recipe method in the service layer"""
    data = ""
    with pytest.raises(ValidationError):
        recipe_service.create_recipe(data)

def test_get_recipes():
    """This function tests the get recipes method in the service layer"""
    result = recipe_service.get_recipes()
    assert result is not None

def test_delete_recipe_by_id_when_recipe_id_exist():
    """This function tests the delete recipe by id method in the service layer"""
    recipe_id = "83e3fe01-a502-4328-8bee-fed6dc72616a"
    assert recipe_service.delete_recipe_by_id(recipe_id) is None

def test_delete_recipe_by_id_when_recipe_id_dont_exist():
    """This function tests the delete recipe by id method in the service layer"""
    recipe_id = "incorrect_id"
    with pytest.raises(RecipeNotFound):
        recipe_service.delete_recipe_by_id(recipe_id)

def test_regenerate_recipe():
    """This function tests the regenerate recipe method in the service layer"""
    assert recipe_service.regenerate_recipe() is None