import pandas as pd
import numpy as np

def read_csv_to_dataframe(file_name):
    return pd.read_csv(file_name, parse_dates=['Date'], index_col='Date')

def calculate_beta_from_csv(stock_csv, index_csv, start_date, end_date):
    # Read data from CSV files
    stock_data = read_csv_to_dataframe(stock_csv)['Adj Close']
    index_data = read_csv_to_dataframe(index_csv)['Adj Close']

    # Filter data based on date range
    stock_data = stock_data.loc[start_date:end_date]
    index_data = index_data.loc[start_date:end_date]

    # Calculate daily returns
    stock_return = stock_data.pct_change().dropna()
    index_return = index_data.pct_change().dropna()

    # Align data by date
    aligned_data = pd.concat([stock_return, index_return], axis=1).dropna()
    aligned_data.columns = ['Stock', 'Index']

    # Calculate mean returns
    stock_mean = aligned_data['Stock'].mean()
    index_mean = aligned_data['Index'].mean()

    # Calculate excess returns
    aligned_data['Excess_Stock'] = aligned_data['Stock'] - stock_mean
    aligned_data['Excess_Index'] = aligned_data['Index'] - index_mean

    # Calculate covariance and variance
    covariance = np.cov(aligned_data['Excess_Stock'], aligned_data['Excess_Index'])[0][1]
    variance = np.var(aligned_data['Excess_Index'], ddof=1)

    # Calculate beta
    beta = covariance / variance

    return beta

# Define stock and index CSV files and the time range
stock_csv = 'C:\\Users\\Nick\\Desktop\\Programming\\python\\stock strats\\beta\\AMD.csv'
index_csv = 'C:\\Users\\Nick\\Desktop\\Programming\\python\\stock strats\\beta\\NASDAQ.csv'
start_date = '2022-09-15'
end_date = '2023-09-15'

# Calculate and print the beta
beta_value = calculate_beta_from_csv(stock_csv, index_csv, start_date, end_date)
print(f"The 1-year beta value based on the given CSV files is: {beta_value}")