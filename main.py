import requests

API_KEY = "API_KEY"
BASE_URL = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base=EUR&symbols=USD"

def euro_to_usd(euro_amount, exchange_rate):
    usd_amount = euro_amount * exchange_rate
    return usd_amount

# Benutzereingabe für den Euro-Betrag
euro_input = float(input("Gib den Betrag in Euro ein: "))

try:
    response = requests.get(BASE_URL)
    data = response.json()

    if "rates" in data and "USD" in data["rates"]:
        usd_exchange_rate = data["rates"]["USD"]
        usd_result = euro_to_usd(euro_input, usd_exchange_rate)
        print(f"{euro_input} Euro entsprechen {usd_result:.2f} US-Dollar")
    else:
        print("Der Wechselkurs für US-Dollar wurde nicht gefunden.")
except requests.exceptions.RequestException as e:
    print(f"Fehler beim Abrufen der Daten von der API: {e}")

