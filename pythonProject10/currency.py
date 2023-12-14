import requests

def convert_currency():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    rates = data["rates"]
    print("Available currencies:")
    for currency in rates:
        print(currency)
    from_currency = input("Enter from currency: ").upper()
    to_currency = input("Enter to currency: ").upper()
    amount = float(input("Enter amount: "))
    if from_currency == "USD":
        converted_amount = amount * rates[to_currency]
        print(f"{amount} USD = {converted_amount:.2f} {to_currency}")
    elif to_currency == "USD":
        converted_amount = amount / rates[from_currency]
        print(f"{amount} {from_currency} = {converted_amount:.2f} USD")
    else:
        converted_amount = amount / rates[from_currency] * rates[to_currency]
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

convert_currency()