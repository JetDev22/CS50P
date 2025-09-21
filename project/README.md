# YOUR PROJECT TITLE
#### Video Demo:
https://youtu.be/DXNdAEpckzU
#### Description:
This is my final project for CS50P.
It is a CLI (comand line interface) Bitcoin Portfolio Tracker that uses the data you enter, requests the current bitcoin price from coincap.io (in USD) and gives you a brief overview of how your Portfolio is doing.

The get started it will ask you for:
- BTC owened (Here you can enter a Float)
- Average Price (The average price for all your coins, this can be found in your exchange account)
- DCA Amount (Your Dollar-Cost-Average amount in USD you invest regulary)

External Modules used:
rich - to get a progress bar for the reload
termgraph - to display the bars displaying your portfolio


Here is a small summary of the functions:
```
def clearScreen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')
```
This function just checks if your are on windows or any other operating system and then depending of the os uses the correct syntax to clear the terminal to make room for this beautiful little program

```
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
```
The getRate function does what the name implies. It gets the api key for coincap.io as argument and then requests the latest bitcoin price. The price is extracted from the returned json and then returned. Should the request fail (due to connection errors for example), the function will return a string and quit the program.

```
def calcROI(value, cost):
    try:
        roi = round((value-cost)/cost*100, 2)
        return roi
    except ZeroDivisionError:
        print("Coins or Average Price was 0")
        sys.exit(1)
```
This function calculated your return of investment and hands it back as return value

```
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
```
Both portfolioValue and portfolioCost are self explanatory. In both TypeErrors are handled and will quit the program if encountered

```
def dcaYield(dca, rate):
    try:
        dcaAmount = round(dca / rate, 5)
        return dcaAmount
    except TypeError:
        print("Problem while calculating")
        sys.exit(1)
```
This function will calculate how many satoshis you will get at the current price with your dollar cost average investment amount (DCA).

```
def printPortfolio(apiKey, coins, avg, dca):
    try:
        while True:
            clearScreen()
            rate = getRate(apiKey)
            value = portfolioValue(coins, rate)
            cost = portfolioCost(coins, avg)
            roi = calcROI(value, cost)
            dcaAmount = dcaYield(dca, rate)
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
```
Here we have the main program loop. The try block is used to capture the users keyboard interupt to exit the program by CTRL+C in a smooth way and avoid the python message that we interrupted the loop. data defines the data used for our graph powered by termgraph (as per their documentation). The args are used to style the graph. I then print a small info for the user, how he can exit the program and the proceed to show a progress bar, to indicate to the use, when the next btc price update is pulled from coincap.io
