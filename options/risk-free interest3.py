# Risk-Free Rate Calculator for Options Contracts
# This script calculates the risk-free rate for an options contract by interpolating U.S. Treasury yields
# and adjusting for inflation. The value is then scaled to correspond to large sums of money.
# A high real risk-free rate value is generally more favorable as it serves as a more attractive baseline for returns.

def interpolate_rate(r_short, t_short, r_long, t_long, t_target):
    """
    Linearly interpolates the yield for the target time period.
    """
    return r_short + ((t_target - t_short) / (t_long - t_short)) * (r_long - r_short)

def main():
    # Hard-coded U.S. Treasury yields for 3-month and 1-year (in percentage terms)
    r_3month = 0.5  # Example: 0.5% for 3-month
    r_1year = 1.0   # Example: 1.0% for 1-year

     # Option expiration period in days
    t_option_days = 150
    # Convert days to months for calculation (approx. 30.42 days in a month)
    t_option_months = t_option_days / 30.42
    t_option_years = t_option_months / 12.0
    
    # Time to expiration for 3-month and 1-year T-Bills in years
    t_3month = 3 / 12.0
    t_1year = 1.0
    
    # Interpolate the yield for the option expiration period
    r_option = interpolate_rate(r_3month, t_3month, r_1year, t_1year, t_option_years)
    
    # Current inflation rate (in percentage terms, e.g., 2%)
    inflation_rate = 2.0
    
    # Calculate the real risk-free rate (in percentage terms)
    real_risk_free_rate = r_option - inflation_rate
    
    # Scale the real risk-free rate for large sums of money (e.g., 1 million dollars as 1.00)
    scaled_real_risk_free_rate = real_risk_free_rate * 10

    print(f"Interpolated yield for {t_option_months}-month option: {r_option:.2f}%")
    print(f"Real risk-free rate: {real_risk_free_rate:.2f}%")
    print(f"Scaled real risk-free rate (where 1 million dollars corresponds to 1.00): {scaled_real_risk_free_rate:.2f}")

if __name__ == "__main__":
    main()
