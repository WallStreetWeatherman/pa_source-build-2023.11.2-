# Retention Ratio Calculator
# --------------------------
# Overview:
# The Retention Ratio, also known as the Plowback Ratio or Retained Earnings Ratio, 
# indicates the proportion of net income that's retained in the company, rather than paid out as dividends.
# It reflects a company's decision to either reinvest profits or to return them to shareholders.
#
# Formula:
# Retention Ratio = 1 - (Dividends per Share (DPS) / Earnings per Share (EPS))
#
# Desired Value:
# A higher retention ratio suggests that the company is reinvesting more of its profits for growth.
# A lower ratio indicates that more profits are being distributed to shareholders.
# The 'ideal' value depends on the company's growth strategy and the stage in its lifecycle.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Earnings per Share (EPS) (This might be in dollars and cents format, so no conversion may be needed, but we'll consider it in millions for this example)
eps_in_millions = 0.07  # Example value representing an EPS of $70,000
eps = convert_to_actual_value(eps_in_millions)

# Dividends per Share (DPS) (in million dollars format)
dps_in_millions = 0.03  # Example value representing a DPS of $30,000
dps = convert_to_actual_value(dps_in_millions)

# Calculate Retention Ratio
retention_ratio = 1 - (dps / eps)

# Output the results
print(f"Retention Ratio: {retention_ratio:.2%}")

if retention_ratio > 0.6:  # Assuming 60% as a general threshold
    print("The company has a high Retention Ratio, indicating that a significant portion of its earnings is being reinvested for future growth.")
else:
    print("The company has a lower Retention Ratio, suggesting that a larger portion of earnings is being distributed to shareholders as dividends.")
