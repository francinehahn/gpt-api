"""Test Summary Service"""
import pytest
from marshmallow import ValidationError
from api.errors.SummaryErrors import SummaryNotFound
from api.services.SummaryService import SummaryService
from tests.mocks.mock_summary_database import MockSummaryDatabase
from tests.mocks.mock_openai import OpenAIMock
from tests.mocks.mock_authentication import AuthenticationMock

summary_service = SummaryService(MockSummaryDatabase(), AuthenticationMock, OpenAIMock)

def test_create_summary_method_when_input_is_correct():
    """This function tests the create summary method in the service layer"""
    data = {'text': "O dólar americano é uma das moedas mais importantes no mundo. Atualmente, sua hegemonia é incontestável, já que é usada na adoção de reservas internacionais por Bancos Centrais de inúmeros países e como referência em qualquer negócio em nível global. Entretanto, nem sempre foi assim. Na verdade, a hegemonia da moeda norte-americana é relativamente recente, pois só se deu após o fim da Segunda Guerra Mundial. O dólar foi idealizado a partir da necessidade de criação de uma moeda que fosse capaz de financiar a Guerra da Independência dos Estados Unidos, em 1776, e fomentar a nova nação. Assim, em 1786 o Congresso Continental das já independentes 13 colônias aprovou o dólar como moeda nacional. O nome dollar vem da palavra thaler, uma conhecida moeda de prata que circulava na Europa durante o século XV. Todavia, até a metade do século XIX, período em que a libra esterlina tinha status de moeda internacional, os Estados Unidos eram considerados devedores de pouca credibilidade no cenário internacional e, ao contrário da maioria dos países europeus, não havia em sua Constituição nenhuma lei que desse ao Estado o controle exclusivo da emissão de moeda. Essa falta de legislação, inclusive, levou a uma situação caótica, pois propiciou a existência sem controle de inúmeras formas de pagamento. Para se ter uma ideia, qualquer indivíduo podia abrir um banco e emitir cédulas sem nenhuma autorização ou controle do governo. A primeira tentativa de unificação dos pagamentos partiu das necessidades de financiamento da Guerra de Secessão, em 1861. Desta forma, o governo passou a emitir notas que, baseadas em sua boa-fé e reputação, poderiam ser convertidas em ouro: as chamadas greenbacks, nome até hoje dado de forma informal ao dólar. A unificação da moeda como forma de pagamento se deu somente em 1863, com o National Banking Act."}
    result = summary_service.create_summary(data)
    assert result is not None

def test_create_summary_method_when_input_is_not_correct():
    """This function tests the create summary method in the service layer"""
    data = ""
    with pytest.raises(ValidationError):
        summary_service.create_summary(data)

def test_get_summaries():
    """This function tests the get summaries method in the service layer"""
    result = summary_service.get_summaries()
    assert result is not None

def test_delete_summary_by_id_when_summary_id_exist():
    """This function tests the delete summary by id method in the service layer"""
    summary_id = "83e3fe01-a502-4328-8bee-fed6dc72616a"
    assert summary_service.delete_summary_by_id(summary_id) is None

def test_delete_summary_by_id_when_summary_id_dont_exist():
    """This function tests the delete summary by id method in the service layer"""
    summary_id = "incorrect_id"
    with pytest.raises(SummaryNotFound):
        summary_service.delete_summary_by_id(summary_id)

def test_regenerate_summary():
    """This function tests the regenerate summary method in the service layer"""
    assert summary_service.regenerate_summary() is None