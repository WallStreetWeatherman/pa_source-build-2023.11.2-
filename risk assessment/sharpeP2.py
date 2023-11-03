# Sharpe Ratio for a Portfolio with Dynamic Weighting from Multiple CSV Files
# Brief Overview: This script calculates the Sharpe Ratio for a portfolio based on historical stock prices from multiple CSV files.
# Desired Value: Higher values of Sharpe Ratio suggest better risk-adjusted returns.

import numpy as np
import pandas as pd

def fetch_stock_data_from_csv(files_dict):
    # Fetch stock data for given tickers from multiple CSV files
    # Each CSV file should contain daily closing prices with a 'Date' column and an 'Adj Close' column for the ticker.
    adj_close_df = pd.DataFrame()
    for ticker, file_path in files_dict.items():
        df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
        adj_close_df[ticker] = df['Adj Close']  # Ensure your CSV has 'Adj Close' as column header
    return adj_close_df

def calculate_daily_returns(adj_close_data):
    # Calculate daily returns
    daily_returns = adj_close_data.pct_change()
    return daily_returns.dropna()

def calculate_sharpe_ratio(portfolio_returns, risk_free_rate, trading_days=252):
    # Calculate the excess returns by subtracting the daily risk-free rate from the daily returns
    excess_daily_returns = portfolio_returns - (risk_free_rate / trading_days)
    
    # Calculate the annualized return and standard deviation
    annual_return = excess_daily_returns.mean() * trading_days
    annual_std_dev = excess_daily_returns.std() * np.sqrt(trading_days)
    
    # Calculate Sharpe Ratio
    sharpe_ratio = annual_return / annual_std_dev
    return sharpe_ratio

if __name__ == "__main__":
    # User-defined inputs
    # Dictionary mapping tickers to their respective CSV file paths
    files_dict = {
        'AAPL': 'path_to_AAPL_data.csv',
        'GOOGL': 'path_to_GOOGL_data.csv',
        'MSFT': 'path_to_MSFT_data.csv',
        # Add more tickers and their file paths as needed
    }
    risk_free_rate = 0.01  # Annual risk-free rate, replace with the current rate
    
    # Fetch stock data from multiple CSV files
    adj_close_data = fetch_stock_data_from_csv(files_dict)
    
    # Calculate daily returns for each stock
    daily_returns = calculate_daily_returns(adj_close_data)
    
    # Calculate portfolio returns based on dynamic weights
    # For simplicity, we're using equal weighting; replace with your own weighting logic if needed
    weights = np.array([1/len(files_dict)] * len(files_dict))
    portfolio_returns = daily_returns.dot(weights)
    
    # Calculate Sharpe ratio for the portfolio
    sharpe_ratio_result = calculate_sharpe_ratio(portfolio_returns, risk_free_rate)
    
    # Output the Sharpe Ratio
    print(f"Sharpe Ratio of the Portfolio: {sharpe_ratio_result}")
