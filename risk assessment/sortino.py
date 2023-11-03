# Sortino Ratio Calculation Script for Portfolio
# Brief Overview: This script calculates the Sortino Ratio, emphasizing downside risk.
# Desired Value: A higher Sortino Ratio is better as it signifies better risk-adjusted returns.
import pandas as pd
import numpy as np

def fetch_stock_data_from_csv(file_path, tickers):
    # Fetch stock data for given tickers from a CSV file
    # The CSV file should contain daily closing prices with a 'Date' column and columns for each ticker.
    df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    # Select only the 'Adj Close' columns we are interested in
    adj_close_df = pd.DataFrame(index=df.index)
    for ticker in tickers:
        adj_close_df[ticker] = df[f'{ticker} Adj Close']
    return adj_close_df

def calculate_daily_returns(price_data):
    daily_returns = price_data.pct_change()
    daily_returns = daily_returns[1:]
    return daily_returns

def calculate_sortino_ratio(daily_returns, target_rate=0, trading_days=252):
    # Calculate the mean of daily returns above the target rate
    mean_return = daily_returns[daily_returns > target_rate].mean()
    
    # Calculate downside deviation
    downside_returns = daily_returns[daily_returns < target_rate]
    downside_std_dev = np.sqrt(np.mean(downside_returns**2))
    
    # Annualize metrics
    mean_return_annualized = mean_return * trading_days
    downside_std_dev_annualized = downside_std_dev * np.sqrt(trading_days)
    
    # Calculate Sortino Ratio
    sortino_ratio = (mean_return_annualized - target_rate) / downside_std_dev_annualized
    
    return sortino_ratio

if __name__ == "__main__":
    # User-defined inputs
    tickers = ['AAPL', 'GOOGL', 'MSFT']
    file_path = 'your_stock_data.csv'  # Replace this with your CSV file path
    
    # Set the annual MAR to 8%
    annual_target_rate = 0.08  # The annual minimum acceptable return (MAR) (8% annual return for s&p 500)

    # Convert the annual MAR to a daily MAR assuming 252 trading days
    daily_target_rate = (1 + annual_target_rate) ** (1/252) - 1
    
    # Fetch stock data
    stock_data = fetch_stock_data_from_csv(file_path, tickers)
    
    # Calculate daily returns
    daily_returns = calculate_daily_returns(stock_data)
    
    # Calculate Sortino ratio
    sortino_ratio_result = calculate_sortino_ratio(daily_returns, daily_target_rate)
    
    # Output results
    print(f"Sortino Ratio: {sortino_ratio_result}")