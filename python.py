def track_portfolio():
    # Hardcoded dictionary defining base stock prices
    stock_prices = {"AAPL": 180, "TSLA": 250, "MSFT": 420, "AMZN": 175, "NVDA": 120}
    portfolio = {}
    
    print("=== CodeAlpha Stock Portfolio Tracker ===")
    print("Available stocks to track:", ", ".join(stock_prices.keys()))
    
    while True:
        symbol = input("\nEnter Stock Symbol (or type 'done' to finish): ").upper().strip()
        if symbol == "DONE":
            break
        if symbol not in stock_prices:
            print("❌ Stock symbol not recognized in system ticker database.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity of shares for {symbol}: "))
            if quantity <= 0:
                print("❌ Quantity must be a positive integer.")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("❌ Invalid input. Quantity must be a whole number.")

    # Calculate Total Investments
    print("\n--- Portfolio Summary ---")
    total_value = 0
    report_lines = ["Stock,Quantity,Price,Total_Value\n"]
    
    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        subtotal = qty * price
        total_value += subtotal
        line_item = f"{symbol}: {qty} shares @ ${price} each = ${subtotal:.2f}"
        print(line_item)
        report_lines.append(f"{symbol},{qty},{price},{subtotal}\n")
        
    print(f"\n💰 Total Portfolio Value: ${total_value:.2f}")
    
    # Optional File Handling Execution Block
    save_file = input("\nWould you like to save this statement to a file? (y/n): ").lower().strip()
    if save_file == 'y':
        filename = "portfolio_report.csv"
        with open(filename, "w") as file:
            file.writelines(report_lines)
            file.write(f"\nTotal Portfolio Value,,,{total_value}")
        print(f"💾 Report safely saved to local workspace as '{filename}'!")

if __name__ == "__main__":
    track_portfolio()
