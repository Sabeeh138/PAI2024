# Exchange rates 
exchange_rates = {
    'USD': 1.0,       # US Dollar
    'EUR': 0.92,      # Euro
    'PKR': 299.0,     # Pakistani Rupee
    'INR': 82.6,      # Indian Rupee
    'JPY': 146.5      # Japanese Yen
}


def display_currencies():
    print("Available currencies:")
    for currency in exchange_rates:
        print(currency)


def convert_currency(amount, from_currency, to_currency):
    usd_amount = amount / exchange_rates[from_currency]
    converted_amount = usd_amount * exchange_rates[to_currency]
    return converted_amount



    print("Welcome to the Currency Converter!")
    display_currencies()

    from_currency = input("Enter the currency you want to convert from (e.g., USD, EUR): ").upper()
    if from_currency not in exchange_rates:
        print("Invalid currency! Please restart and choose a valid one.")
        return
    
    try:
        amount = float(input(f"Enter the amount in {from_currency}: "))
    except ValueError:
        print("Invalid amount! Please enter a numeric value.")
        return

    
    to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR): ").upper()
    if to_currency not in exchange_rates:
        print("Invalid currency! Please restart and choose a valid one.")
        return

    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")


