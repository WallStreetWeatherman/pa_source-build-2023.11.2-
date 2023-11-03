# Sharpe Ratio Calculation Script
# Brief Overview: This script calculates the Sharpe Ratio of an investment portfolio.
# Desired Value: The higher the Sharpe Ratio, the better the risk-adjusted return.

import pandas as pd
import numpy as np

def fetch_stock_data(tickers, start_date, end_date):
    # Simulate fetching stock data for given tickers and date range
    # Replace this function with actual stock data fetching logic
    dates = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=dates)
    for ticker in tickers:
        df[ticker] = np.random.randn(len(dates))  # Simulated price data
    return df

def calculate_daily_returns(price_data):
    # Calculate daily returns
    daily_returns = price_data.pct_change()
    daily_returns = daily_returns[1:]  # Remove first row of NaN
    return daily_returns

def calculate_sharpe_ratio(daily_returns, risk_free_rate, trading_days=252):
    # Calculate the portfolio's Sharpe ratio
    mean_daily_return = daily_returns.mean()
    daily_std_dev = daily_returns.std()
    
    # Annualize the metrics
    mean_return_annualized = mean_daily_return * trading_days
    std_dev_annualized = daily_std_dev * np.sqrt(trading_days)
    
    # Calculate Sharpe Ratio
    sharpe_ratio = (mean_return_annualized - risk_free_rate) / std_dev_annualized
    return sharpe_ratio

if __name__ == "__main__":
    # User-defined inputs
    tickers = ['AAPL', 'GOOGL', 'MSFT']
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    risk_free_rate = 0.01  # Annual risk-free rate, typically based on 10-year Treasury yield
    
    # Fetch stock data
    stock_data = fetch_stock_data(tickers, start_date, end_date)
    
    # Calculate daily returns
    daily_returns = calculate_daily_returns(stock_data)
    
    # Calculate portfolio Sharpe ratio
    sharpe_ratio_result = calculate_sharpe_ratio(daily_returns, risk_free_rate)
    
    # Output the results
    print(f"Sharpe Ratio: {sharpe_ratio_result}")

if sharpe_ratio_result >= 1.0:
    print("The portfolio's Sharpe Ratio is strong, indicating a higher risk-adjusted return.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. High Return: The portfolio is generating returns significantly higher than the risk-free rate.")
    print("2. Lower Volatility: Indicates effective risk management in portfolio selection.")
    
elif sharpe_ratio_result >= 0.5:
    print("The portfolio's Sharpe Ratio is moderate, further improvements can be made.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Moderate Returns: Returns are decent but there's room for improvement.")
    print("2. Average Volatility: The portfolio is neither too risky nor too safe, optimize for better returns.")
    
else:
    print("The portfolio's Sharpe Ratio is low, indicating poor risk-adjusted returns.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Low Returns: The returns are not justifying the risks taken.")
    print("2. High Volatility: The portfolio's high volatility is adversely affecting its Sharpe Ratio.")
    print("3. Risk-free rate: A high risk-free rate can also pull down the Sharpe Ratio if the returns aren't compensating for the additional risk.")
    