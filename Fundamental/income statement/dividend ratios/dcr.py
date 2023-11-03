# Dividend Coverage Ratio Calculator
# ----------------------------------
# Overview:
# The Dividend Coverage Ratio indicates how well a company's earnings can cover its dividend payments to shareholders.
# It provides insight into the sustainability of a company's dividend policy.
#
# Formula:
# Dividend Coverage Ratio = Earnings per Share (EPS) / Dividends per Share (DPS)
#
# Desired Value:
# A higher ratio indicates that the company can easily cover its dividends using its earnings.
# A ratio less than 1 suggests that the company is not generating enough earnings to cover its dividends, which may be unsustainable in the long run.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Earnings per Share (EPS) (This might be in dollars and cents format, so no conversion may be needed, but we'll consider it in millions for this example)
eps_in_millions = 0.08  # Example value representing an EPS of $80,000
eps = convert_to_actual_value(eps_in_millions)

# Dividends per Share (DPS) (in million dollars format)
dps_in_millions = 0.04  # Example value representing a DPS of $40,000
dps = convert_to_actual_value(dps_in_millions)

# Calculate Dividend Coverage Ratio
dividend_coverage_ratio = eps / dps

# Output the results
print(f"Dividend Coverage Ratio: {dividend_coverage_ratio:.2f}")

if dividend_coverage_ratio >= 2:  # Assuming 2 as a general threshold
    print("The company has a high Dividend Coverage Ratio, indicating that it can comfortably cover its dividend payments from its earnings.")
else:
    print("The company has a lower Dividend Coverage Ratio, suggesting potential difficulty in maintaining current dividend levels if earnings decrease.")
