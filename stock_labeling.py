stock_data = {
    "AAPL": {"yesterday": 232.00, "today": 231.19},
    "TSLA": {"yesterday": 334.00, "today": 330.1501},
    "MSFT": {"yesterday": 522.00, "today": 520.35},
    "NVDA": {"yesterday": 181.00, "today": 179.74}
}
price_changes = {ticker: ((data["today"] - data["yesterday"]) / data["yesterday"] * 100) 
                 for ticker, data in stock_data.items()}
labels = {ticker: ("Down" if change < -1 else "Up" if change > 1 else "Stable") 
          for ticker, change in price_changes.items()}
print("Stock price change labels (based on last Friday, Aug 15, 2025):")
for ticker, label in labels.items():
    print(f"{ticker}: {label} ({price_changes[ticker]:.2f}%)")
