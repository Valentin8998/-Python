import requests
from config import key

url = 'https://yougile.com/api-v2'

header = {
        'Authorization': key
    }


def test_post():
    project = {
        'title': 'проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    resp = requests.post(url+'/projects', headers=header, json=project)
    assert resp.status_code == 201
    project_id = resp.json()['id']
    # Очистка
    project = {
        'deleted': True,
        'title': 'проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    delete = requests.put(
        url + "/projects/" + project_id, headers=header, json=project
        )
    assert delete.status_code == 200


def test_put():
    project = {
        'title': 'проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    resp = requests.post(url+'/projects', headers=header, json=project)
    assert resp.status_code == 201
    # Получаем id из ответа
    project_id = resp.json()['id']

    update_project = {
        'title': 'изменённый проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    resl = requests.put(
        url + "/projects/" + project_id, headers=header, json=update_project
        )
    assert resl.status_code == 200
    # Очистка
    project = {
        'deleted': True,
        'title': 'проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    delete = requests.put(
        url + "/projects/" + project_id, headers=header, json=project
        )
    assert delete.status_code == 200


def test_get():
    project = {
        'title': 'проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    resp = requests.post(url+'/projects', headers=header, json=project)
    assert resp.status_code == 201
    # Получаем id из ответа
    project_id = resp.json()['id']
    resl = requests.get(
        url + "/projects/" + project_id, headers=header
        )
    assert resl.status_code == 200
    # Очистка
    project = {
        'deleted': True,
        'title': 'проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    delete = requests.put(
        url + "/projects/" + project_id, headers=header, json=project
        )
    assert delete.status_code == 200


def test_401():
    heade = {
        'Authorization': 'token'
    }
    project = {
        'title': 'проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    resp = requests.post(url+'/projects', headers=heade, json=project)
    assert resp.status_code == 401


def test_404():
    project = {
        'title': 'проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    resp = requests.post(
        url+'/projects'+'123abc', headers=header, json=project
        )
    assert resp.status_code == 404


def test_absence_haders():
    project = {
        'title': 'проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    resp = requests.post(
        url+'/projects', json=project
        )
    assert resp.status_code == 401


def test_get_with_invalid_id():
    invalid_id = "invalid_id_123"
    resp = requests.get(url + "/projects/" + invalid_id, headers=header)
    # 1. Проверка статус-кода
    assert resp.status_code == 404  # Или 400, зависит от API
    # 2. Проверка сообщения об ошибке в теле ответа
    error_body = resp.json()
    assert "error" in error_body or "message" in error_body, (
     "Тело ответа не содержит описание ошибки"
    )


def test_put_without_auth():
    project = {
        'title': 'проект',
        'users': {'a91959fa-0614-4ef0-9dcd-220ae0a2493c': 'admin'}
    }
    resp = requests.post(url+'/projects', headers=header, json=project)
    assert resp.status_code == 201
    # Получаем id из ответа
    project_id = resp.json()['id']
    # Не передаём headers или передаём пустые
    resp = requests.put(
        url + "/projects/" + project_id,
        json=project
    )
    assert resp.status_code == 401  # Unauthorized
    # Обязательная проверка тела ошибки
    error_body = resp.json()
    assert "error" in error_body or "message" in error_body, (
     "Нет сообщения об ошибке при 401"
    )
