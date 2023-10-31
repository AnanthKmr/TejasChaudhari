# import pytest
# from unittest.mock import patch, Mock
# from Pokeapi import PokemonInfoRetriever
#
#
# @pytest.fixture
# def mock_pokemon_info_retriever():
#     with patch('Pokeapi.PokemonInfoRetriever.requests.get') as mock_get:
#         mock_instance = PokemonInfoRetriever()
#         mock_instance.pokemon_name = 'pikachu'
#         mock_instance._PokemonInfoRetriever__url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
#         yield mock_instance


import pytest
from unittest.mock import patch, Mock
from requests.exceptions import RequestException
from Pokeapi import PokemonInfoRetriever


@pytest.fixture
def mock_pokemon_info_retriever():
    with patch('requests.get') as mock_get:
        mock_instance = PokemonInfoRetriever()
        mock_instance.pokemon_name = 'pikachu'
        mock_instance._PokemonInfoRetriever__url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
        yield mock_instance
