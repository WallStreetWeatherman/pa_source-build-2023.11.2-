import yfinance as yf
stock = yf.Ticker("AAPL")
print(stock.info)