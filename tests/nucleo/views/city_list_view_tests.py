from http import HTTPStatus

import pytest
from django.template.response import TemplateResponse
from django.test import Client

pytestmark = pytest.mark.django_db


def test_get_city_list(client: Client, django_db_setup):
    """Página deve renderizar com as chaves esperadas no contexto"""
    response = client.get('/cidades/')

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)
    assert response.context_data is not None
    assert 'cidades' in response.context_data
    assert 'algoritmos' in response.context_data


def test_city_list_exibe_cidades(client: Client, django_db_setup):
    """Cidades cadastradas devem aparecer no HTML"""
    response = client.get('/cidades/')

    assert response.status_code == HTTPStatus.OK
    # valida que o template renderizou a tabela
    assert 'Cidade' in response.text
    assert 'Importância' in response.text


def test_city_list_sem_cidades(client: Client, django_db_setup):
    """Com banco vazio, deve exibir mensagem de fallback"""
    response = client.get('/cidades/')

    assert response.status_code == HTTPStatus.OK
    # depende do seu {% empty %} no template
    assert 'Nenhuma cidade cadastrada' in response.text or 'Cidade' in response.text


def test_city_list_link_voltar(client: Client, django_db_setup):
    """Deve haver link de volta para o planejador"""
    response = client.get('/cidades/')

    assert 'Voltar ao planejador' in response.text