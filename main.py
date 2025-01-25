
#Import Libraries and Configure API
import requests
import json

API_KEY = "MDFUIX9QYS9L160I"
BASE_URL = "https://www.alphavantage.co/query" 



#Fetch Real-Time Stock Data

def get_stock_price(symbol):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    try:
        price = float(data["Global Quote"]["05. price"])
        return price
    except KeyError:
        print("Error: Could not fetch stock data. Check the symbol or API limits.")
        return None



#Portfolio Management 
portfolio = {}

def add_stock(symbol, quantity, buy_price):
    portfolio[symbol] = {
        "quantity": quantity,
        "buy_price": buy_price
    }

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
    else:
        print(f"Stock {symbol} not found in portfolio.")



#Calculate Performance

def portfolio_summary():
    total_value = 0
    total_invested = 0
    print("\nPortfolio Summary:")
    print(f"{'Symbol':<10}{'Quantity':<10}{'Buy Price':<15}{'Current Price':<15}{'Profit/Loss':<10}")
    
    for symbol, details in portfolio.items():
        current_price = get_stock_price(symbol)
        if current_price:
            quantity = details["quantity"]
            buy_price = details["buy_price"]
            current_value = current_price * quantity
            invested = buy_price * quantity
            profit_loss = current_value - invested
            
            total_value += current_value
            total_invested += invested
            
            print(f"{symbol:<10}{quantity:<10}{buy_price:<15}{current_price:<15}{profit_loss:<10.2f}")
    
    print(f"\nTotal Invested: {total_invested}")
    print(f"Total Portfolio Value: {total_value}")
    print(f"Total Profit/Loss: {total_value - total_invested}")



#Run the tool

if __name__ == "__main__":
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            buy_price = float(input("Enter buy price: "))
            add_stock(symbol, quantity, buy_price)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == "3":
            portfolio_summary()
        elif choice == "4":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

