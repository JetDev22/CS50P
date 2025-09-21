import requests
import os
import sys
import time
from rich.progress import track
from termgraph import Data, Args, BarChart
from logo import logo


def main():
    apiKey = "Insert your own key"

    try:
        coins = float(input("BTC owened: "))
        avg = float(input("Average Price: "))
        dca = float(input("DCA Amount: "))
    except ValueError:
        print("\nERROR!\nOnly enter numbers\nPlease try again")
        sys.exit(1)
    rate = getRate(apiKey)
    value = portfolioValue(coins, rate)
    cost = portfolioCost(coins, avg)
    roi = calcROI(value, cost)
    dcaAmount = dcaYield(dca, rate)
    printPortfolio(value, cost, dcaAmount)


def clearScreen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


def getRate(apiKey):
    try:
        getPrice = requests.get(
            f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={apiKey}")
        answer = getPrice.json()
        price = round(float(answer["data"]["priceUsd"]), 2)
        return price
    except requests.RequestException:
        print("Request to Coincap failed")
        sys.exit(1)


def calcROI(value, cost):
    try:
        roi = round((value-cost)/cost*100, 2)
        return roi
    except ZeroDivisionError:
        print("Coins or Average Price was 0")
        sys.exit(1)


def portfolioValue(coins, rate):
    try:
        value = round(coins * rate, 2)
        return value
    except TypeError:
        print("Problem while calculating")
        sys.exit(1)


def portfolioCost(coins, avg):
    try:
        cost = round(coins * avg, 2)
        return cost
    except TypeError:
        print("Problem while calculating")
        sys.exit(1)


def dcaYield(dca, rate):
    try:
        dcaAmount = round(dca / rate, 5)
        return dcaAmount
    except TypeError:
        print("Problem while calculating")
        sys.exit(1)


def printPortfolio(value, cost, dcaAmount):
    try:
        while True:
            clearScreen()
            winLoss = value - cost
            data = Data([[cost], [value], [winLoss]], [
                        "Portfolio Cost", "Portfolio Value", "Portfolio Yield"])
            args = Args(title="Portfolio Performance",
                        width=50, format="{:.0f}", suffix=" USD")
            print(logo)
            chart = BarChart(data, args)
            chart.draw()
            print("\n")
            print(f"Your current DCA gives you {dcaAmount} BTC\n")
            print("=> Press CTRL+C to exit <=\n")
            for i in track(range(20), description="Next Update..."):
                time.sleep(1)
    except KeyboardInterrupt:
        print("Thank you for using my little programm. See you soon")


if __name__ == "__main__":
    main()
