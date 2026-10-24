
import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name! Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment

    portfolio.append([stock_name, quantity, price, investment])

    print(f"Investment in {stock_name}: ${investment}")

# Display portfolio summary
print("\n===== PORTFOLIO SUMMARY =====")
print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Investment'}")

for stock, quantity, price, investment in portfolio:
    print(f"{stock:<10}{quantity:<10}${price:<9}${investment}")

print(f"\nTotal Investment: ${total_investment}")

# Save portfolio to CSV
with open("stock_portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Price", "Investment"])
    writer.writerows(portfolio)
    writer.writerow(["", "", "Total Investment", total_investment])

print("\nPortfolio saved to stock_portfolio.csv")
