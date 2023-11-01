from Exchange_rates_api import ExchangeRateFetcher

if __name__ == "__main__":
    api_key = "ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8"

    exchange_rate_fetcher = ExchangeRateFetcher(api_key)

    while True:
        base_currency = input("Enter the base currency (e.g., USD, EUR, GBP) or 'exit' to quit: ")
        if base_currency.lower() == 'exit':
            break
        result = exchange_rate_fetcher.get_exchange_rates(base_currency)
        print(result)