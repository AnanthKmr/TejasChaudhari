import unittest
from unittest.mock import patch
from Exchange_rates_api import get_exchange_rates


class TestGetExchangeRates(unittest.TestCase):

    @patch('Exchange_rates_api.requests.get')
    def test_successful_request(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "base": "USD",
            "rates": {"EUR": 0.85, "GBP": 0.75}
        }

        result = get_exchange_rates("USD")
        expected_output = "Exchange rates for USD:\nEUR: 0.85\nGBP: 0.75\n"

        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_failed_request(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        result = get_exchange_rates("USD")
        expected_output = "Failed to retrieve exchange rate information. Status code: 404\n"

        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_missing_rates_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "base": "USD"
        }

        result = get_exchange_rates("USD")
        expected_output = "No exchange rate data found.\n"

        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_invalid_base_currency(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "error": "Invalid base currency"
        }

        result = get_exchange_rates("XYZ")
        expected_output = "Failed to retrieve exchange rate information. Error: Invalid base currency\n"

        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_empty_base_currency(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 400

        result = get_exchange_rates("")
        expected_output = "Failed to retrieve exchange rate information. Status code: 400\n"

        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_connection_error(self, mock_get):
        mock_get.side_effect = ConnectionError

        result = get_exchange_rates("USD")
        expected_output = "Failed to retrieve exchange rate information. Connection Error.\n"

        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_non_json_response(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")

        result = get_exchange_rates("USD")
        expected_output = "Failed to retrieve exchange rate information. Invalid JSON response.\n"

        self.assertEqual(result, expected_output)

    @patch('Exchange_rates_api.requests.get')
    def test_timeout_error(self, mock_get):
        mock_get.side_effect = TimeoutError("Request timed out")

        result = get_exchange_rates("USD")
        expected_output = "Failed to retrieve exchange rate information. Request timed out.\n"

        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()