import pandas as pd
import matplotlib.pyplot as plt

def fetch_data_from_csv(filename):
    historical_data = pd.read_csv(filename, parse_dates=['Date'], index_col='Date')
    return historical_data

def calculate_z_scores(historical_data, window=20):
    historical_data['Moving_Avg'] = historical_data['Close'].rolling(window=window).mean()
    historical_data['Std_Dev'] = historical_data['Close'].rolling(window=window).std()
    z_scores = (historical_data['Close'] - historical_data['Moving_Avg']) / historical_data['Std_Dev']
    return z_scores

def mean_reversion_analysis(daily_data, weekly_data, monthly_data, 
                            ebitda_margin, operating_income,
                            current_ratio, long_term_debt_to_equity_ratio,
                            free_cash_flow, roe, asset_turnover, ev_to_ebitda,
                            z_threshold=2.0):
    daily_z = calculate_z_scores(daily_data)
    weekly_z = calculate_z_scores(weekly_data)
    monthly_z = calculate_z_scores(monthly_data)

    weekly_z = weekly_z.reindex(daily_data.index, method='ffill')
    monthly_z = monthly_z.reindex(daily_data.index, method='ffill')

    signals = pd.DataFrame(index=daily_data.index)
    signals['price'] = daily_data['Close']
    signals['signal'] = 0.0

    signals['Daily_Z'] = daily_z
    signals['Weekly_Z'] = weekly_z
    signals['Monthly_Z'] = monthly_z

    if (ebitda_margin > 0.1 and
        operating_income > 0 and  
        current_ratio > 1.0 and  
        long_term_debt_to_equity_ratio < 0.5 and  
        free_cash_flow > 0 and  
        roe > 0.1 and  
        asset_turnover > 0.5 and  
        ev_to_ebitda < 10):

        signals.loc[(signals['Daily_Z'] > z_threshold) & 
                    (signals['Weekly_Z'] > z_threshold) & 
                    (signals['Monthly_Z'] > z_threshold), 'signal'] = 1.0

        signals.loc[(signals['Daily_Z'] < -z_threshold) & 
                    (signals['Weekly_Z'] < -z_threshold) & 
                    (signals['Monthly_Z'] < -z_threshold), 'signal'] = -1.0

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
    ticker = "HIMS"  
    daily_filename = "C:\\Users\\Nick\\Desktop\\Programming\\python\\historical data CSVs\\stocks\\HIMS_daily.csv"
    weekly_filename = "C:\\Users\\Nick\\Desktop\\Programming\\python\\historical data CSVs\\stocks\\HIMS_weekly.csv"
    monthly_filename = "C:\\Users\\Nick\\Desktop\\Programming\\python\\historical data CSVs\\stocks\\HIMS_monthly.csv"

    daily_data = fetch_data_from_csv(daily_filename)
    weekly_data = fetch_data_from_csv(weekly_filename)
    monthly_data = fetch_data_from_csv(monthly_filename)

    ebitda_margin = -41.36
    operating_income = -44770000
    current_ratio = 3.53
    long_term_debt_to_equity_ratio = 1.6
    free_cash_flow = 17830000
    roe = -14.7
    asset_turnover = 1.82
    ev_to_ebitda = -30.86

    signals = mean_reversion_analysis(daily_data, weekly_data, monthly_data,
                                     ebitda_margin, operating_income,
                                     current_ratio, long_term_debt_to_equity_ratio,
                                     free_cash_flow, roe, asset_turnover, ev_to_ebitda)

    plot_signals(signals, ticker)
