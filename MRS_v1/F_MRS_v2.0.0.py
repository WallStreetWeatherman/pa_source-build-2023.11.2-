import pandas as pd
import matplotlib.pyplot as plt

def fetch_data_from_csv(filename):
    historical_data = pd.read_csv(filename, parse_dates=['Date'], index_col='Date')
    return historical_data

def mean_reversion_analysis(historical_data, pe_ratio, z_threshold=2.0, pe_threshold=20.0):
    window = 20
    historical_data['Moving_Avg'] = historical_data['Close'].rolling(window=window).mean()
    historical_data['Std_Dev'] = historical_data['Close'].rolling(window=window).std()

    signals = pd.DataFrame(index=historical_data.index)
    signals['price'] = historical_data['Close']
    signals['signal'] = 0.0

    signals['z-score'] = (signals['price'] - historical_data['Moving_Avg']) / historical_data['Std_Dev']

    if pe_ratio < pe_threshold:
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
    ticker = "HIMS"  # Replace with the ticker of your choice
    filename = "C:\\Users\Nick\\Desktop\Programming\\python\\historical data CSVs\\stocks\\HIMS_daily.csv"
    pe_ratio = 18.0  # Replace with the P/E ratio

    historical_data = fetch_data_from_csv(filename)
    signals = mean_reversion_analysis(historical_data, pe_ratio)
    plot_signals(signals, ticker)
