import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'

@pytest.fixture
def token():
    token = os.getenv('TOKEN')
    if not token:
        pytest.fail('YANDEX_TOKEN не установлен в переменных окружения')
    return token

@pytest.fixture
def headers(token):
    return {'Authorization': f'OAuth {token}'}

@pytest.fixture
def params():
    return {'path': 'disk:/temp_folder'}

@pytest.fixture
def create_and_delete_folder(headers, params):

    # Создание папки.
    response = requests.put(BASE_URL, headers=headers, params=params)
    if response.status_code not in [201, 409]:
        pytest.fail(f'Ошибка при создании папки: {response.text}')

    yield

    # Удаление папки.
    response2 = requests.delete(BASE_URL, headers=headers,
                                params={'path': 'disk:/temp_folder', 'permanently': 'true'})
    if response2.status_code not in [202, 204]:
        pytest.fail(f'Ошибка при удалении папки: {response2.text}')

def test_create_folder_success(create_and_delete_folder, headers, params):
    response = requests.put(BASE_URL, headers=headers, params=params)
    assert response.status_code in [201, 409]

def test_folder_existing(create_and_delete_folder, headers, params):
    response = requests.put(BASE_URL, headers=headers, params=params)
    assert response.status_code == 409

def test_invalid_data(headers):
    response = requests.put(BASE_URL, headers=headers, params={'path': 'yd-disk:/temp_folder'})
    assert response.status_code == 400

def test_not_autorized(params):
    response = requests.put(BASE_URL, params=params)
    assert response.status_code == 401

def test_invalid_path(headers):
    response = requests.put(BASE_URL, headers=headers, params={'path': 'disk:////////'})
    assert response.status_code == 404


