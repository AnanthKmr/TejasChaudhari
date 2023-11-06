# import requests
#
#
# def get_exchange_rates(base_currency):
#     api_url = f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency}"
#
#
#     api_key = "ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8"
#
#     headers = {
#         "apikey": api_key,
#     }
#
#     response = requests.get(api_url, headers=headers)
#
#     if response.status_code == 200:
#         exchange_rate_data = response.json()
#         rates = exchange_rate_data.get("rates")
#
#         if rates:
#             print(f"Exchange rates for {base_currency}:")
#             for currency, rate in rates.items():
#                  print(f"{currency}: {rate}")
#         else:
#             print("No exchange rate data found.")
#     else:
#         print("Failed to retrieve exchange rate information. Status code:", response.status_code)
#
# if __name__ == "__main__":
#     base_currency = input("Enter the base currency (e.g., USD, EUR, GBP): ")
#     get_exchange_rates(base_currency)

#  *******Working*******
# import requests
#
#
# def get_exchange_rates(base_currency):
#     api_url = f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency}"
#     api_key = "ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8"
#     headers = {
#         "apikey": api_key,
#     }
#
#     try:
#         response = requests.get(api_url, headers=headers)
#         response.raise_for_status()
#
#         exchange_rate_data = response.json()
#         rates = exchange_rate_data.get("rates")
#
#         if rates:
#             output = f"Exchange rates for {base_currency}:\n"
#             for currency, rate in rates.items():
#                 output += f"{currency}: {rate}\n"
#             return output
#         else:
#             return "No exchange rate data found."
#
#     except requests.exceptions.ConnectionError:
#         return "Failed to retrieve exchange rate information. Connection Error."
#
#     except requests.exceptions.Timeout:
#         return "Failed to retrieve exchange rate information. Request timed out."
#
#     except requests.exceptions.RequestException as e:
#         return f"Failed to retrieve exchange rate information. Error: {str(e)}"
#
#     except ValueError as e:
#         return f"Failed to retrieve exchange rate information. Invalid JSON response: {str(e)}"
#
#
# if __name__ == "__main__":
#     base_currency = input("Enter the base currency (e.g., USD, EUR, GBP): ")
#     print(get_exchange_rates(base_currency))


# import requests
#
#
# class ExchangeRateFetcher:
#     def __init__(self, api_key):
#         self.api_key = api_key
#
#     def get_exchange_rates(self, base_currency):
#         api_url = f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency}"
#         headers = {
#                     "apikey": self.api_key,
#         }
#
#         try:
#             response = requests.get(api_url, headers=headers)
#             response.raise_for_status()  # Raise an exception for HTTP errors
#             exchange_rate_data = response.json()
#             rates = exchange_rate_data.get("rates")
#             if rates:
#                 output = f"Exchange rates for {base_currency}:\n"
#                 for currency, rate in rates.items():
#                     output += f"{currency}: {rate}\n"
#                 return output
#             else:
#                 return "No exchange rate data found."
#         except requests.exceptions.ConnectionError:
#             return "Failed to retrieve exchange rate information. Connection Error."
#         except requests.exceptions.Timeout:
#             return "Failed to retrieve exchange rate information. Request timed out."
#         except requests.exceptions.RequestException as e:
#             print(f"RequestException:{str(e)}")
#             return f"Failed to retrieve exchange rate information. Error: {str(e)}"
#         except ValueError as e:
#             return f"Failed to retrieve exchange rate information. Invalid JSON response: {str(e)}"
#
# if __name__ == "__main__":
#     api_key = "ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8"
#     exchange_rate_fetcher = ExchangeRateFetcher(api_key)
#
#     while True:
#         base_currency = input("Enter the base currency (e.g., USD, EUR, GBP) or 'exit' to quit: ")
#         if base_currency.lower() == 'exit':
#             break
#         result = exchange_rate_fetcher.get_exchange_rates(base_currency)
#         print(result)

#
# import requests
#
#
# class ExchangeRateFetcher:
#     def __init__(self, api_key):
#         self.api_key = api_key
#
#     def get_exchange_rates(self, base_currency):
#         api_url = f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency}"
#         headers = {
#                     "apikey": self.api_key,
#         }
#         try:
#             response = requests.get(api_url, headers=headers)
#             response.raise_for_status()  # Raise an exception for HTTP errors
#
#             if response.status_code == 404:
#                 return "Failed to retrieve exchange rate information. Status code: 404"
#
#             exchange_rate_data = response.json()
#             rates = exchange_rate_data.get("rates")
#             if rates:
#                 output = f"Exchange rates for {base_currency}:\n"
#                 for currency, rate in rates.items():
#                     output += f"{currency}: {rate}\n"
#                 return output
#             else:
#                 return "No exchange rate data found."
#         except requests.exceptions.ConnectionError:
#             return "Failed to retrieve exchange rate information. Connection Error."
#         except requests.exceptions.Timeout:
#             return "Failed to retrieve exchange rate information. Request timed out."
#         except requests.exceptions.RequestException as e:
#             return f"Failed to retrieve exchange rate information. Error: {str(e)}"
#         except ValueError as e:
#             return f"Failed to retrieve exchange rate information. Invalid JSON response: {str(e)}"


import requests


class ExchangeRateFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.apilayer.com/exchangerates_data"


    def get_exchange_rates(self, base_currency):
        if not base_currency:
            return "Invalid base currency."

        url = f"{self.base_url}/latest?base={base_currency}"
        headers = {
            "apikey": self.api_key,
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            exchange_rate_data = response.json()
            return exchange_rate_data
        elif response.status_code == 401:
            return "Authentication error"
        elif response.status_code == 404:
            return "Failed to retrieve exchange rate information. Status code: 404"
        elif response.status_code == 204:
            return "No exchange rate data found."
        elif response.status_code == 400:
            return "Invalid base currency."
        else:
            return f"Failed to retrieve exchange rate information. Status code: {response.status_code}"

    def get_currency_conversion(self, from_currency, to_currency, amount):
        if not from_currency or not to_currency:
            return "Invalid currency conversion request."

        url = f"{self.base_url}/convert?from={from_currency}&to={to_currency}&amount={amount}"
        headers = {
            "apikey": self.api_key,
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            conversion_data = response.json()
            return conversion_data

        # Handle other status codes here
        elif response.status_code == 401:
            return "Authentication error"
        elif response.status_code == 404:
            return "Failed to retrieve currency conversion information. Status code: 404"
        elif response.status_code == 201:
            return "No currency conversion data found."
        elif response.status_code == 400:
            return "No currency conversion data found."
        else:
            return f"Failed to retrieve currency conversion information. Status code: {response.status_code}"



def retrieve_exchange_rates(base_currency, api_key):
    fetcher = ExchangeRateFetcher(api_key)
    return fetcher.get_exchange_rates(base_currency)


if __name__ == "__main__":
    api_key = "ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8"
    while True:
        base_currency = input("Enter the base currency (e.g., USD, EUR) or type 'EXIT' to exit: ").upper()
        if base_currency == "EXIT":
            break

        exchange_rate_data = retrieve_exchange_rates(base_currency, api_key)

        if exchange_rate_data == "Authentication error":
            print("Authentication error. Invalid API key.")
        elif exchange_rate_data == "Failed to retrieve exchange rate information. Status code: 404":
            print("Failed to retrieve exchange rate information. Status code: 404")
        elif exchange_rate_data == "No exchange rate data found.":
            print("No exchange rate data found.")
        elif exchange_rate_data == "Failed to retrieve exchange rate information. Status code: 400":
            print("Failed to retrieve exchange rate information. Status code: 400")
        elif "rates" in exchange_rate_data:
            rates = exchange_rate_data["rates"]
            print(f"Exchange rates for {base_currency}:")
            for currency, rate in rates.items():
                print(f"{currency}: {rate}")
        else:
            print("Invalid base currency.")