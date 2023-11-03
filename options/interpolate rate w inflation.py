def interpolate_rate(r_short, t_short, r_long, t_long, t_target):
    """
    Linearly interpolates the yield for the target time period.
    """
    return r_short + ((t_target - t_short) / (t_long - t_short)) * (r_long - r_short)

# Define the yields for the shorter and longer-term T-Bills (in percentage form)
r_short = 5.45  # 5.45% for 3-month
r_long = 5.52  # 5.52% for 6-month

# Define the time to expiration for the shorter and longer-term T-Bills (in years)
t_short = 3 / 12.0  # 3 months
t_long = 6 / 12.0  # 6 months

# Time to expiration for the option in days
t_option_days = 116  # Example: 117 days

# Convert it to months for the calculation. Assume 30 days in a month for simplicity.
t_option_months = t_option_days / 30.0

# Convert it to years for further calculation
t_target = t_option_months / 12.0  

# Perform the interpolation
r_option = interpolate_rate(r_short, t_short, r_long, t_long, t_target)

# Define the inflation rate (in percentage form)
inflation_rate = 3.7  # Example: 2%

# Adjust for inflation to get the real risk-free rate
real_risk_free_rate = r_option - inflation_rate

print(f"Interpolated risk-free rate for {t_option_days}-day option: {r_option:.4f}%")
print(f"Real risk-free rate after accounting for inflation: {real_risk_free_rate:.4f}%")
