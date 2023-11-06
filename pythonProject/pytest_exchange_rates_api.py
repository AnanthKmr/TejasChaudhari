# import pytest
# from Exchange_rates_api import ExchangeRateFetcher
#
# api_key = "ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8"
# fetcher = ExchangeRateFetcher(api_key)
#
#
# @pytest.mark.test
# def test_successful_request():
#     base_currency = "USD"
#     response = fetcher.get_exchange_rates(base_currency)
#     assert "rates" in response
#     assert response["base"] == base_currency
#     assert response["success"] is True
#     assert response["timestamp"] is not None
#     assert "date" in response
#     assert "rates" in response
#
#
# @pytest.mark.test
# def test_authentication_error():
#     api_key = "invalid_api_key"
#     fetcher = ExchangeRateFetcher(api_key)
#     base_currency = "USD"
#     response = fetcher.get_exchange_rates(base_currency)
#     assert response == "Authentication error"
#
#
# @pytest.mark.test
# def test_invalid_base_currency():
#     invalid_base_currency = "INVALID"
#     response = fetcher.get_exchange_rates(invalid_base_currency)
#     assert response == "Failed to retrieve exchange rate information. Status code: 400"
#
#
# @pytest.mark.test
# def test_no_exchange_rate_data():
#     base_currency = "jp"
#     response = fetcher.get_exchange_rates(base_currency)
#     assert response == "Failed to retrieve exchange rate information. Status code: 400"
#
#
# @pytest.mark.test
# def test_nonexistent_currency_conversion():
#     base_currency = "USD"
#     target_currency = "ABC"  # A currency that does not exist
#     response = fetcher.get_exchange_rates(base_currency)
#     assert "error" in response  # Modify this assertion to match the structure of the API response
#
#
# # Add more test cases for other scenarios
#
# if __name__ == "__main__":
#     pytest.main(["-v", "pytest_exchange_rates_api.py"])


import pytest
from requests import RequestException

from Exchange_rates_api import ExchangeRateFetcher


class TestExchangeRateFetcher:
    api_key = "ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8"

    @pytest.fixture
    def fetcher(self):
        return ExchangeRateFetcher(self.api_key)

    def test_successful_request(self, fetcher):
        base_currency = "USD"
        response = fetcher.get_exchange_rates(base_currency)
        assert "rates" in response

    def test_authentication_error(self, fetcher):
        invalid_api_key = "invalid_api_key"
        fetcher.api_key = invalid_api_key
        response = fetcher.get_exchange_rates("USD")
        assert response == "Authentication error"

    def test_invalid_base_currency(self, fetcher):
        response = fetcher.get_exchange_rates("INVALID")
        assert "Invalid base currency." in response

    def test_non_existent_currency_conversion(self, fetcher):
        response = fetcher.get_currency_conversion("USD", "NONEXISTENT", 100)
        assert "No currency conversion data found." in response


    def test_currency_conversion(self, fetcher):
        response = fetcher.get_currency_conversion("USD", "EUR", 100)
        assert isinstance(response, dict)
        assert "result" in response
        assert response["result"] > 0

    def test_successful_request_with_specific_base_currency(self, fetcher):
        base_currency = "EUR"
        response = fetcher.get_exchange_rates(base_currency)
        assert "rates" in response
        assert response["base"] == base_currency

    def test_successful_currency_conversion(self, fetcher):
        from_currency = "USD"
        to_currency = "EUR"
        amount = 100
        response = fetcher.get_currency_conversion(from_currency, to_currency, amount)
        assert "result" in response
        assert response["result"] > 0


    def test_authentication_error_currency_conversion(self, fetcher):
        fetcher.api_key = "invalid_api_key"
        from_currency = "USD"
        to_currency = "EUR"
        amount = 100
        response = fetcher.get_currency_conversion(from_currency, to_currency, amount)
        assert response == "Authentication error"

    def test_no_currency_conversion_data(self, fetcher):
        from_currency = "USD"
        to_currency = "EUR"
        amount = -100  # Negative amount
        response = fetcher.get_currency_conversion(from_currency, to_currency, amount)
        assert response == "No currency conversion data found."

    def test_empty_base_currency(self, fetcher):
        response = fetcher.get_exchange_rates("")
        assert response == "Invalid base currency."

    def test_netwrok_error(selfself,fetcher):
        fetcher.base_url = "http://nonexistent-url.com"
        with pytest.raises(RequestException):
            fetcher.get_exchange_rates("usd")