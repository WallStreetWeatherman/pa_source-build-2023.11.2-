# Sharpe Ratio for a Portfolio
# This script calculates the Sharpe Ratio for a portfolio consisting of multiple stocks.
# A high Sharpe Ratio value indicates a better risk-adjusted return.
# We use synthetic historical stock prices for this example.

import numpy as np
import pandas as pd

# Create synthetic data for 3 stocks in the portfolio
dates = pd.date_range('2021-01-01', '2021-12-31')
stock_A = np.random.normal(loc=0.0005, scale=0.02, size=len(dates))
stock_B = np.random.normal(loc=0.0003, scale=0.015, size=len(dates))
stock_C = np.random.normal(loc=0.0004, scale=0.018, size=len(dates))

# Construct the portfolio
portfolio_df = pd.DataFrame({'Stock_A': stock_A, 'Stock_B': stock_B, 'Stock_C': stock_C}, index=dates)

# Portfolio weights (replace with your own)
weights = np.array([0.4, 0.3, 0.3])

# Calculate portfolio returns
portfolio_df['Portfolio_Return'] = portfolio_df.dot(weights)

# Risk-free rate (annualized, replace with current rate)
risk_free_rate = 0.01

# Calculate annualized portfolio return and standard deviation
annual_return = np.mean(portfolio_df['Portfolio_Return']) * 252
annual_std_dev = np.std(portfolio_df['Portfolio_Return']) * np.sqrt(252)

# Calculate Sharpe Ratio
sharpe_ratio = (annual_return - risk_free_rate) / annual_std_dev
print(f"Sharpe Ratio of the Portfolio: {sharpe_ratio}")
