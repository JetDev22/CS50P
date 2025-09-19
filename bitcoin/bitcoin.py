import requests
import sys

apiKey = "9b027259644109058f17effe0d1557adc9709fd7a60955cef9d2c554f9b26df8"

try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Arg must be integer or float")

try:
    getPrice = requests.get(
        f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={apiKey}")
except requests.RequestException:
    print("Request to Coincap failed")

answer = getPrice.json()
price = float(answer["data"]["priceUsd"])
print(f"${(price*bitcoin):,.4f}", end="")
