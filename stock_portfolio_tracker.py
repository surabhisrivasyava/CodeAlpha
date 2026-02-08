# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

total_investment = 0

print("Stock Portfolio Tracker")

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
    else:
        print("Stock not available")

print("Total Investment Value: ₹", total_investment)

# File handling with UTF-8 encoding (FIXED)
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")
    file.write("Total Investment Value: ₹" + str(total_investment))

print("Result saved successfully in portfolio.txt")
