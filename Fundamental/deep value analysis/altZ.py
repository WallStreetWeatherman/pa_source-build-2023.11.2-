# Altman Z-Score Calculator
# --------------------------
# Overview:
# The Altman Z-Score is a financial metric used to predict the likelihood of a company going 
# into bankruptcy. It is based on five weighted financial ratios calculated from data on a 
# company's financial statements.
#
# Formula:
# Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E
#
# Where:
# A = Working Capital / Total Assets
# B = Retained Earnings / Total Assets
# C = Earnings Before Interest & Taxes / Total Assets
# D = Market Value of Equity / Total Liabilities
# E = Sales / Total Assets
#
# Desired Value:
# Z > 2.99 - Safe Zone (low probability of bankruptcy)
# 1.81 < Z < 2.99 - Grey Zone (uncertain probability)
# Z < 1.81 - Distress Zone (high probability of bankruptcy)
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# financial statement data should be input.

# Representing financial values in millions as decimals
working_capital = 5.00  # Represents $5 million
total_assets = 30.00  # Represents $30 million
retained_earnings = 10.00  # Represents $10 million
ebit = 2.00  # Represents $2 million
market_value_equity = 12.00  # Represents $12 million
total_liabilities = 18.00  # Represents $18 million
sales = 20.00  # Represents $20 million

# Calculating the components for the Altman Z-Score
A = working_capital / total_assets
B = retained_earnings / total_assets
C = ebit / total_assets
D = market_value_equity / total_liabilities
E = sales / total_assets

# Calculating the Altman Z-Score
z_score = 1.2*A + 1.4*B + 3.3*C + 0.6*D + 1.0*E

# Outputting the results
print(f"Altman Z-Score: {z_score:.2f}")
if z_score > 2.99:
    print("Safe Zone: Low probability of bankruptcy.")
elif 1.81 < z_score < 2.99:
    print("Grey Zone: Uncertain probability of bankruptcy.")
else:
    print("Distress Zone: High probability of bankruptcy.")
