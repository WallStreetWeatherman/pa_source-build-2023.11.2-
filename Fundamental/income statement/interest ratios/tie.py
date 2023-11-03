# Interest Coverage Ratio (Times Interest Earned) Calculator
# ---------------------------------------------------------
# Overview:
# The Interest Coverage Ratio measures a company's ability to cover its interest obligations with its operating profit.
# It provides insight into the financial health and creditworthiness of a company.
#
# Formula:
# Interest Coverage Ratio = Earnings Before Interest and Taxes (EBIT) / Interest Expense
#
# Desired Value:
# A higher ratio indicates that the company can easily meet its interest obligations from its operating profits.
# A lower ratio suggests potential difficulty in meeting interest obligations, which may lead to solvency issues.
# Generally, a ratio below 1.5 may indicate potential liquidity concerns.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Earnings Before Interest and Taxes (EBIT) (in million dollars format)
ebit_in_millions = 15.00  # Example value representing an EBIT of $15,000,000
ebit = convert_to_actual_value(ebit_in_millions)

# Interest Expense (in million dollars format)
interest_expense_in_millions = 2.00  # Example value representing an interest expense of $2,000,000
interest_expense = convert_to_actual_value(interest_expense_in_millions)

# Calculate Interest Coverage Ratio
interest_coverage_ratio = ebit / interest_expense

# Output the results
print(f"Interest Coverage Ratio: {interest_coverage_ratio:.2f}")

if interest_coverage_ratio >= 1.5:  # Assuming 1.5 as a general threshold
    print("The company has a high Interest Coverage Ratio, indicating that it can comfortably cover its interest obligations from its operating profits.")
else:
    print("The company has a lower Interest Coverage Ratio, suggesting potential difficulty in meeting interest obligations. This might raise liquidity concerns.")
