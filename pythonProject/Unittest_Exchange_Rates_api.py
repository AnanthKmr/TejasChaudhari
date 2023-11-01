import unittest
from unittest.mock import patch
import requests
from Exchange_rates_api import ExchangeRateFetcher


class TestExchangeRateFetcher(unittest.TestCase):
    @patch('Exchange_rates_api.requests.get')
    def test_successful_request(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "base": "USD",
            "rates": {"EUR": 0.85, "GBP": 0.75}
        }
        fetcher = ExchangeRateFetcher(api_key="ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8")
        result = fetcher.get_exchange_rates("USD")
        expected_output = "Exchange rates for USD:\nEUR: 0.85\nGBP: 0.75\n"
        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_failed_request(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        fetcher = ExchangeRateFetcher(api_key="ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8")
        result = fetcher.get_exchange_rates("USD")
        expected_output = "Failed to retrieve exchange rate information. Status code: 404"
        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError
        fetcher = ExchangeRateFetcher(api_key="ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8")
        result = fetcher.get_exchange_rates("USD")
        expected_output = "Failed to retrieve exchange rate information. Connection Error."
        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_timeout_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout
        fetcher = ExchangeRateFetcher(api_key="ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8")
        result = fetcher.get_exchange_rates("USD")
        expected_output = "Failed to retrieve exchange rate information. Request timed out."
        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_request_exception(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Custom Error")
        fetcher = ExchangeRateFetcher(api_key="ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8")
        result = fetcher.get_exchange_rates("USD")
        expected_output = "Failed to retrieve exchange rate information. Error: Custom Error"
        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_invalid_json_response(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")
        fetcher = ExchangeRateFetcher(api_key="ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8")
        result = fetcher.get_exchange_rates("USD")
        expected_output = "Failed to retrieve exchange rate information. Invalid JSON response: Invalid JSON"
        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_no_exchange_rate_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "base": "USD"
        }
        fetcher = ExchangeRateFetcher(api_key="ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8")
        result = fetcher.get_exchange_rates("USD")
        expected_output = "No exchange rate data found."
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()



