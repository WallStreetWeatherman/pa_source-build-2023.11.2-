# Sharpe Ratio for an Individual Stock
# This script calculates the Sharpe Ratio for an individual stock from a CSV file.
# A high Sharpe Ratio value indicates a better risk-adjusted return.

import numpy as np
import pandas as pd

def fetch_stock_data_from_csv(file_path, ticker):
    # Fetch stock data for a given ticker from a CSV file
    # The CSV file should contain daily closing prices with a 'Date' column and an 'Adj Close' column for the ticker.
    df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    return df[f'{ticker} Adj Close']

def calculate_daily_returns(adj_close_data):
    # Calculate daily returns
    daily_returns = adj_close_data.pct_change()
    return daily_returns.dropna()

def calculate_sharpe_ratio(daily_returns, risk_free_rate, trading_days=252):
    # Calculate the excess returns by subtracting the daily risk-free rate from the daily returns
    excess_daily_returns = daily_returns - (risk_free_rate / trading_days)
    
    # Calculate the annualized return and standard deviation
    annual_return = excess_daily_returns.mean() * trading_days
    annual_std_dev = excess_daily_returns.std() * np.sqrt(trading_days)
    
    # Calculate Sharpe Ratio
    sharpe_ratio = annual_return / annual_std_dev
    return sharpe_ratio

if __name__ == "__main__":
    # User-defined inputs
    ticker = 'AAPL'  # Specify the ticker for the stock you want to analyze
    file_path = 'path_to_your_stock_data.csv'  # Replace with your CSV file path
    risk_free_rate = 0.01  # Annual risk-free rate, replace with the current rate
    
    # Fetch stock data from CSV
    adj_close_data = fetch_stock_data_from_csv(file_path, ticker)
    
    # Calculate daily returns
    daily_returns = calculate_daily_returns(adj_close_data)
    
    # Calculate Sharpe ratio
    sharpe_ratio_result = calculate_sharpe_ratio(daily_returns, risk_free_rate)
    
    # Output results
    print(f"Sharpe Ratio of the {ticker} stock: {sharpe_ratio_result}")