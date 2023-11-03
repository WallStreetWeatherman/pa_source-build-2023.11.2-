# Z-Score (Altman Z-Score) Calculator for Bankruptcy Prediction
# -------------------------------------------------------------
# Overview:
# The Altman Z-Score is a formula for predicting the probability of a company going bankrupt within a two-year time frame.
# It is based on five financial ratios. Edward Altman, a financial economist and professor at New York University, 
# developed it in 1968.
#
# Formula:
# Z-Score = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E
# 
# Where:
# A = Working Capital / Total Assets
# B = Retained Earnings / Total Assets
# C = Earnings Before Interest and Taxes / Total Assets
# D = Market Value of Equity / Total Liabilities
# E = Sales / Total Assets
#
# Desired Value:
# A Z-Score above 3.0 is considered safe, indicating a low probability of bankruptcy.
# A Z-Score below 1.8 suggests a higher risk of bankruptcy.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values (in million dollar format for consistency)

working_capital_in_millions = 10.00  # Example: $10,000,000
total_assets_in_millions = 100.00  # Example: $100,000,000
retained_earnings_in_millions = 20.00  # Example: $20,000,000
ebit_in_millions = 8.00  # Earnings Before Interest and Taxes: Example: $8,000,000
market_value_equity_in_millions = 50.00  # Example: $50,000,000
total_liabilities_in_millions = 60.00  # Example: $60,000,000
sales_in_millions = 120.00  # Example: $120,000,000

# Convert the values
working_capital = convert_to_actual_value(working_capital_in_millions)
total_assets = convert_to_actual_value(total_assets_in_millions)
retained_earnings = convert_to_actual_value(retained_earnings_in_millions)
ebit = convert_to_actual_value(ebit_in_millions)
market_value_equity = convert_to_actual_value(market_value_equity_in_millions)
total_liabilities = convert_to_actual_value(total_liabilities_in_millions)
sales = convert_to_actual_value(sales_in_millions)

# Calculate the Z-Score
A = working_capital / total_assets
B = retained_earnings / total_assets
C = ebit / total_assets
D = market_value_equity / total_liabilities
E = sales / total_assets

z_score = 1.2*A + 1.4*B + 3.3*C + 0.6*D + 1.0*E

# Output the results
print(f"Z-Score: {z_score:.2f}")

if z_score > 3.0:
    print("The company is considered safe from bankruptcy.")
elif z_score < 1.8:
    print("The company is at higher risk of bankruptcy.")
else:
    print("The company is in a grey zone, and its financial health should be reviewed in more detail.")