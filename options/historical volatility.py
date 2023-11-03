import pandas as pd
import numpy as np

def compute_historical_volatility(csv_file):
    # Read the stock price data from a CSV file
    df = pd.read_csv(csv_file)
    
    # Ensure the data is sorted by date (if the data isn't already)
    df = df.sort_values(by="Date")
    
    # Compute logarithmic returns
    df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
    
    # Calculate the annualized volatility
    volatility = df['Log_Return'].std() * np.sqrt(252)  # Assuming 252 trading days in a year
    return volatility

if __name__ == "__main__":
    csv_file = "C:\\Users\\Nick\\Desktop\\Programming\\python\\historical data CSVs\\stocks\\M_1yr.csv"  # Replace with your CSV file name
    sigma = compute_historical_volatility(csv_file)
    print(f"Historical volatility (sigma) for the stock is: {sigma:.4f}")

