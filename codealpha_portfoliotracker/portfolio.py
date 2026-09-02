# Stock Portfolio Tracker

import os

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")

# Display available stocks
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Ask how many different stocks the user wants
num_stocks = int(input("\nHow many stocks do you want to add? "))

portfolio = []

# Take user input
for i in range(num_stocks):
    stock = input(f"\nEnter stock name #{i + 1}: ").upper()

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment
        portfolio.append((stock, quantity, price, investment))

        print(f"{stock} investment value: ${investment}")

    else:
        print("❌ Stock not available in the price list.")

# Display portfolio summary
print("\n===== Portfolio Summary =====")

for stock, quantity, price, investment in portfolio:
    print(
        f"{stock} | Quantity: {quantity} | "
        f"Price: ${price} | Value: ${investment}"
    )

print(f"\n💰 Total Investment: ${total_investment}")

# Ask whether to save the result
save = input(
    "\nDo you want to save the result to a file? (yes/no): "
).lower()

if save == "yes":

    # Save file in the same folder as this Python file
    file_path = os.path.join(
        os.path.dirname(__file__),
        "stock_portfolio.txt"
    )

    with open(file_path, "w") as file:

        file.write("===== Stock Portfolio Tracker =====\n\n")

        for stock, quantity, price, investment in portfolio:
            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Value: ${investment}\n"
            )

        file.write(
            f"\nTotal Investment: ${total_investment}\n"
        )

    print("✅ Portfolio saved successfully!")
    print("📁 File name: stock_portfolio.txt")
