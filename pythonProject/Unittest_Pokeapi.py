# import unittest
# from unittest.mock import patch, Mock
# from requests import Response
# from Pokeapi import get_pokemon_info
#
#
# class TestGetPokemonInfo(unittest.TestCase):
#
#     @patch('requests.get')
#     def test_successful_request(self, mock_get):
#         # Mock a successful response with sample data
#         response = Response()
#         response.status_code = 200
#         response.json = lambda: {
#             "name": "pikachu",
#             "id": 25,
#             "height": 4,
#             "weight": 60,
#             "abilities": [
#                 {"ability": {"name": "static"}},
#                 {"ability": {"name": "lightning-rod"}}
#             ]
#         }
#         mock_get.return_value = response
#
#         # Capture the printed output
#         with unittest.mock.patch('builtins.print') as mock_print:
#             get_pokemon_info("pikachu")
#
#         # Verify the printed output
#         expected_output = [
#             unittest.mock.call('Name:', 'pikachu'),
#             unittest.mock.call('ID:', 25),
#             unittest.mock.call('Height:', 4),
#             unittest.mock.call('Weight:', 60),
#             unittest.mock.call('Abilities:'),
#             unittest.mock.call('- static'),
#             unittest.mock.call('- lightning-rod')
#         ]
#         mock_print.assert_has_calls(expected_output)
#     @patch('requests.get')
#     def test_failed_request(self, mock_get):
#         # Mock a failed request with a 404 status code
#         response = Response()
#         response.status_code = 404
#         mock_get.return_value = response
#
#         # Capture the printed output
#         with unittest.mock.patch('builtins.print') as mock_print:
#             get_pokemon_info("charizard")
#
#         # Verify the printed output
#         expected_output = "Failed to retrieve Pokemon information. Status code: 404"
#         mock_print.assert_called_with(expected_output)
#
#
# if __name__ == '__main__':
#     unittest.main()
# import pytest
# import responses
# from Pokeapi import get_pokemon_info
#
#
# @pytest.fixture
# def mock_responses():
#     with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
#         yield rsps
#
#
# def test_successful_request(mock_responses, capsys):
#     # Mock the successful response
#     mock_responses.add(
#         responses.GET,
#         'https://pokeapi.co/api/v2/pokemon/pikachu/',
#         json={
#             "name": "pikachu",
#             "id": 25,
#             "height": 4,
#             "weight": 60,
#             "abilities": [
#                 {"ability": {"name": "static"}},
#                 {"ability": {"name": "lightning-rod"}}
#             ]
#         },
#         status=200,
#     )
#
#     get_pokemon_info("pikachu")
#
#     captured = capsys.readouterr()
#     expected_output = [
#         'Name: pikachu',
#         'ID: 25',
#         'Height: 4',
#         'Weight: 60',
#         'Abilities:',
#         '- static',
#         '- lightning-rod',
#     ]
#
#     for line in expected_output:
#         assert line in captured.out
#

# if __name__ == '__main__':
#     pytest.main()
import pytest
from unittest.mock import patch, Mock

import requests
from Pokeapi import get_pokemon_info


@pytest.fixture
def mock_requests_get():
    with patch('requests.get') as mock_get:
        yield mock_get


def test_successful_request(mock_requests_get, capsys):
    expected_output = """Name: pikachu
ID: 25
Height: 4
Weight: 60
Abilities:
- static
- lightning-rod"""

    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "name": "pikachu",
        "id": 25,
        "height": 4,
        "weight": 60,
        "abilities": [{"ability": {"name": "static"}}, {"ability": {"name": "lightning-rod"}}]
    }

    mock_requests_get.return_value = response

    get_pokemon_info("pikachu")
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_failed_request(mock_requests_get, capsys):
    expected_output = "Failed to retrieve Pokemon information. Status code: 404"

    response = Mock()
    response.status_code = 404
    mock_requests_get.return_value = response

    get_pokemon_info("mewtwo")
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_no_name_found(capsys):
    expected_output = "Pokemon name cannot be empty."

    get_pokemon_info("")
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_non_json_response(mock_requests_get, capsys):
    expected_output = "Failed to retrieve Pokemon information. Invalid JSON"

    response = Mock()
    response.status_code = 200
    response.json.side_effect = ValueError("Invalid JSON")

    mock_requests_get.return_value = response

    get_pokemon_info("charizard")
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_connection_error(mock_requests_get, capsys):
    expected_output = "Failed to retrieve Pokemon information. Connection error"

    mock_requests_get.side_effect = requests.exceptions.RequestException("Connection error")

    get_pokemon_info("mewtwo")
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


if __name__ == '__main__':
    pytest.main()