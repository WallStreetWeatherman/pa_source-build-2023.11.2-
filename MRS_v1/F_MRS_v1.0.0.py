import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data(ticker):
    stock_data = yf.Ticker(ticker)
    historical_data = stock_data.history(period="1y")
    fundamentals = stock_data.info

    return historical_data, fundamentals

def mean_reversion_analysis(historical_data, fundamentals, z_threshold=2.0, pe_threshold=20.0):
    # Compute moving average and standard deviation
    window = 20
    historical_data['Moving_Avg'] = historical_data['Close'].rolling(window=window).mean()
    historical_data['Std_Dev'] = historical_data['Close'].rolling(window=window).std()

    # Create a DataFrame for signals
    signals = pd.DataFrame(index=historical_data.index)
    signals['price'] = historical_data['Close']
    signals['signal'] = 0.0

    # Compute the z-score based on the moving average and standard deviation
    signals['z-score'] = (signals['price'] - historical_data['Moving_Avg']) / historical_data['Std_Dev']

    # Fundamental Indicator: P/E Ratio
    pe_ratio = fundamentals.get('trailingPE', None)

    if pe_ratio and pe_ratio < pe_threshold:
        signals.loc[signals['z-score'] > z_threshold, 'signal'] = 1.0
        signals.loc[signals['z-score'] < -z_threshold, 'signal'] = -1.0

    return signals

def plot_signals(signals, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(signals['price'], label='Price')
    plt.plot(signals.loc[signals['signal'] == 1.0].index, signals.price[signals['signal'] == 1.0], '^', markersize=10, color='g', label='Buy Signal')
    plt.plot(signals.loc[signals['signal'] == -1.0].index, signals.price[signals['signal'] == -1.0], 'v', markersize=10, color='r', label='Sell Signal')
    plt.title(f'Mean Reversion Signals for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    ticker = "AAPL"  # Replace with the ticker of your choice
    historical_data, fundamentals = fetch_data(ticker)
    signals = mean_reversion_analysis(historical_data, fundamentals)
    plot_signals(signals, ticker)
