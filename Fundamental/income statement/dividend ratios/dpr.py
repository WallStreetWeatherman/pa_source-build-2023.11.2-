# Dividend Payout Ratio Calculator
# --------------------------------
# Overview:
# The Dividend Payout Ratio measures the percentage of earnings a company pays to its shareholders in dividends.
# It helps investors understand how much of the company's earnings are being returned to shareholders versus 
# how much is being reinvested in the company.
#
# Formula:
# Dividend Payout Ratio = Dividends per Share (DPS) / Earnings per Share (EPS)
#
# Desired Value:
# A lower ratio can suggest that the company is reinvesting more into its growth, whereas 
# a higher ratio indicates that more earnings are being distributed to shareholders.
# There's no 'perfect' value, as it depends on the company's strategy and the expectations of its investors.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Earnings per Share (EPS) (This might be in dollars and cents format, so no conversion may be needed, but we'll consider it in millions for this example)
eps_in_millions = 0.05  # Example value representing an EPS of $50,000
eps = convert_to_actual_value(eps_in_millions)

# Dividends per Share (DPS) (in million dollars format)
dps_in_millions = 0.03  # Example value representing a DPS of $30,000
dps = convert_to_actual_value(dps_in_millions)

# Calculate Dividend Payout Ratio
dividend_payout_ratio = dps / eps

# Output the results
print(f"Dividend Payout Ratio: {dividend_payout_ratio:.2%}")

if dividend_payout_ratio > 0.6:  # Assuming 60% as a general threshold
    print("The company has a high Dividend Payout Ratio, indicating that a significant portion of its earnings is being distributed to shareholders.")
else:
    print("The company has a low Dividend Payout Ratio, suggesting that a larger portion of earnings is being reinvested.")
