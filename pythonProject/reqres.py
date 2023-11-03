import requests
import json
import jsonpath
from datetime import datetime

baseUrl = "https://reqres.in/"


def test_fetch_user():
    path = "api/users/2"
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.support.url')[0] == 'https://reqres.in/#support-heading'
    assert jsonpath.jsonpath(responseJson, '$.data.id')[0] == 2


#

def test_fetch_resource():
    path = "api/{resource}?page=2&per_page=3"
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    # assert jsonpath.jsonpath(responseJson,'$.support.url')[0] == 'https://reqres.in/#support-heading'
    # assert jsonpath.jsonpath(responseJson,'$.data.id')[0] == 4
    names = jsonpath.jsonpath(responseJson, '$.data[*].name')
    # print(names)
    assert names[2] == 'blue turquoise'


def test_fetch_resource_id():
    path = "api/{resource}/3"
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.name')[0] == 'true red'
    assert jsonpath.jsonpath(responseJson, '$.data.id')[0] == 3


def test_fetch_users():
    path = "api/users?page=1&per_page=2"
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    first_name = jsonpath.jsonpath(responseJson, '$.data[*].first_name')
    assert first_name[1] == 'Janet'


def test_fetch_user_id():
    path = "api/users/1"
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.first_name')[0] == 'George'
    assert jsonpath.jsonpath(responseJson, '$.data.id')[0] == 1


def test_create_delete_user():
    file = open('C:/Users/tejasc/PycharmProjects/pythonProject/user.json', "r")
    path = "api/users"
    inputData = json.loads(file.read())
    response = requests.post(url=baseUrl + path, json=inputData)
    responseJson = json.loads(response.text)
    assert response.status_code == 201
    assert jsonpath.jsonpath(responseJson, '$.name')[0] == inputData["name"]
    id = jsonpath.jsonpath(responseJson, '$.id')[0]
    response = requests.delete(url=baseUrl + path + '/' + id)
    assert response.status_code == 204


payload = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}


def test_fetch_user():
    path = "api/users/2"
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert payload[0][0] == "2"
    assert jsonpath.jsonpath(responseJson, '$.data.id')[0] == 2


def test_update_user():
    base_url = "https://reqres.in/api"

    user_id = 2
    data = {
        "first_name": "Yash"

    }

    url = f"{base_url}/users/{user_id}"

    response = requests.put(url, json=data)
    assert response.status_code == 200


def test_update_user1():
    # date=
    base_url = "https://reqres.in/api"

    user_id = 2
    data = {
        "first_name": "Sushrut"

    }

    url = f"{base_url}/users/{user_id}"

    response = requests.patch(url, json=data)
    assert response.status_code == 200


def test_update_user2():
    # date=
    base_url = "https://reqres.in/api"

    user_id = 2
    data = {
        "id": 3,
        "email": "janet.weaver@reqres.in",
        "first_name": "Sushrut",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    }

    url = f"{base_url}/users/register"

    response = requests.post(url, json=data)
    assert response.status_code == 201
