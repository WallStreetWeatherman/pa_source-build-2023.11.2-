# Cash to Debt Ratio Calculator with Industry Comparison
# ------------------------------------------------------
# Overview:
# The Cash to Debt Ratio measures a company's ability to repay its total debt with its available cash.
# This script also compares the calculated ratio with the industry average to gauge the company's position relative to its peers.
#
# Formula:
# Cash to Debt Ratio = Cash & Cash Equivalents / Total Debt
#
# Desired Value:
# A high Cash to Debt Ratio indicates better ability to cover debt with available cash. A ratio greater than 1 
# implies that the company can pay off its debt with the cash it has on hand. Comparing to industry average 
# provides a contextual benchmark.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

def convert_to_actual_value(value_in_millions):
    """Convert value where 1 million dollars is represented as 1.00, 10 million as 10.00, etc."""
    return value_in_millions * 1000000

# Hard-coded values for the company
cash_equivalents_in_millions = 438.00  
cash_equivalents = convert_to_actual_value(cash_equivalents_in_millions)

total_debt_in_millions = 5972.00  
total_debt = convert_to_actual_value(total_debt_in_millions)

# Industry averages
industry_avg_cash_equivalents_in_millions = 400.00  # Example value
industry_avg_cash_equivalents = convert_to_actual_value(industry_avg_cash_equivalents_in_millions)

industry_avg_debt_in_millions = 6000.00  # Example value
industry_avg_debt = convert_to_actual_value(industry_avg_debt_in_millions)

# Calculate Cash to Debt Ratios
company_ratio = cash_equivalents / total_debt
industry_avg_ratio = industry_avg_cash_equivalents / industry_avg_debt

# Output the results
print(f"Company's Cash to Debt Ratio: {company_ratio:.2f}")
print(f"Industry Average Cash to Debt Ratio: {industry_avg_ratio:.2f}")

if company_ratio > industry_avg_ratio:
    print("The company's Cash to Debt Ratio is higher than the industry average, suggesting a better liquidity position compared to peers.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Strong Operating Cash Flows: High cash generation from operations.")
    print("2. Conservative Debt Management: Lower amounts of short-term or high-interest debt.")
    print("3. Divestment: Sale of non-core assets increases cash reserves.")
else:
    print("The company's Cash to Debt Ratio is below the industry average, indicating potential liquidity concerns relative to the industry.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Capital Expenditures: Heavy investment in long-term projects reduces available cash.")
    print("2. Poor Working Capital Management: Inefficient use of short-term assets and liabilities.")
    print("3. Seasonal Business: Cash flow may be low during off-peak seasons.")