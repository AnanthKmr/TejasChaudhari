import requests


def get_exchange_rates(base_currency):
    api_url = f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency}"


    api_key = "ybH5SHckJKrkM9Ln0oYpBKlKhr55kPI8"  # Replace with your API key

    headers = {
        "apikey": api_key,
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        exchange_rate_data = response.json()
        rates = exchange_rate_data.get("rates")

        if rates:
            print(f"Exchange rates for {base_currency}:")
            for currency, rate in rates.items():
                 print(f"{currency}: {rate}")
        else:
            print("No exchange rate data found.")
    else:
        print("Failed to retrieve exchange rate information. Status code:", response.status_code)

if __name__ == "__main__":
    base_currency = input("Enter the base currency (e.g., USD, EUR, GBP): ")
    get_exchange_rates(base_currency)