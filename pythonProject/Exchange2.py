from Exchange_rates_api import ExchangeRateFetcher


if __name__ == "__main__":
    api_key = "ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8"
    fetcher = ExchangeRateFetcher(api_key)

    while True:
        base_currency = input("Enter the base currency (e.g., USD, EUR) or type 'EXIT' to exit: ").upper()
        if base_currency == "EXIT":
            break

        exchange_rate_data = fetcher.get_exchange_rates(base_currency)

        if "rates" in exchange_rate_data:
            rates = exchange_rate_data["rates"]
            print(f"Exchange rates for {base_currency}:")
            for currency, rate in rates.items():
                print(f"{currency}: {rate}")
        elif exchange_rate_data == "Authentication error":
            print("Authentication error. Invalid API key.")
        elif exchange_rate_data == "Failed to retrieve exchange rate information. Status code: 400":
            print("Failed to retrieve exchange rate information. Status code: 400")
        elif exchange_rate_data == "No exchange rate data found.":
            print("No exchange rate data found.")
        else:
            print("Invalid base currency.")
