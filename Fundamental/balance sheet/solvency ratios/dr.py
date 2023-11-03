# Debt Ratio Calculator
# ---------------------
# Overview:
# The Debt Ratio measures the proportion of a company's assets that are financed by debt. 
# It provides an indication of the company's financial leverage and ability to cover its 
# liabilities with its assets.
#
# Formula:
# Debt Ratio = Total Liabilities / Total Assets
#
# Desired Value:
# A higher Debt Ratio indicates that a larger proportion of the company's assets are 
# financed by debt, which can be riskier. A lower ratio suggests that the company relies 
# more on equity to finance its assets, which can be seen as safer. However, a very low 
# ratio might suggest that the company is not leveraging its assets to its fullest potential.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Debt Ratio Calculator with Industry Comparisons and Contextual Information
def convert_to_actual_value(value_in_millions):
    """Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc."""
    return value_in_millions * 1000000

# Hard-coded values for the company
total_assets_in_millions = 16304.00  # Example: $16.3 billion
total_assets = convert_to_actual_value(total_assets_in_millions)
total_liabilities_in_millions = 12094.00  # Example: $12.1 billion
total_liabilities = convert_to_actual_value(total_liabilities_in_millions)

# Hard-coded values for industry average
industry_avg_assets_in_millions = 15000.00  # Example: $15 billion
industry_avg_assets = convert_to_actual_value(industry_avg_assets_in_millions)
industry_avg_liabilities_in_millions = 11000.00  # Example: $11 billion
industry_avg_liabilities = convert_to_actual_value(industry_avg_liabilities_in_millions)

# Calculate Debt Ratio
debt_ratio = total_liabilities / total_assets
industry_avg_debt_ratio = industry_avg_liabilities / industry_avg_assets

print(f"Company's Debt Ratio: {debt_ratio:.2f}")
print(f"Industry Average Debt Ratio: {industry_avg_debt_ratio:.2f}")

# Interpretation
if debt_ratio > industry_avg_debt_ratio:
    print("The company has a higher Debt Ratio than the industry average, indicating a greater reliance on debt financing.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Aggressive Growth Strategy: The company might be borrowing to fuel rapid expansion.")
    print("2. Interest Rate Risk: The company may face challenges if interest rates rise.")
elif debt_ratio < industry_avg_debt_ratio:
    print("The company has a lower Debt Ratio than the industry average, which could signify a more conservative financing approach.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Strong Cash Reserves: The company might have ample liquidity, reducing the need for debt.")
    print("2. Suboptimal Asset Utilization: A very low ratio could indicate that the company is not leveraging its assets effectively.")
else:
    print("The company's Debt Ratio is in line with the industry average.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Balanced Financing: The company is neither too aggressive nor too conservative in its financing structure.")
    print("2. Market Conformity: The company follows industry norms in its capital structure.")
