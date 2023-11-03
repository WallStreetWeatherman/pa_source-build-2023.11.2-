# Debt to Equity Ratio Calculation
# --------------------------------
# Overview:
# The Debt to Equity Ratio measures a company's financial leverage by comparing its total debt to total equity. 
# It gives an insight into the way a company finances its operations and the potential risk associated with its leverage.
#
# Desired Value:
# A lower Debt to Equity Ratio indicates that the company has less risk associated with its debt load. However, what is 
# considered a "good" ratio can vary widely by industry. Generally, ratios greater than 1 indicate more debt financing than equity,
# which could be risky, but it's essential to compare against industry standards.

# Hardcoded values for the company (in the format where 1 million is represented as 1.00, etc.)
company_total_debt = 150.00  # e.g., $150 million of total debt
company_total_equity = 200.00  # e.g., $200 million of total equity

# Hardcoded values for the industry average
industry_average_total_debt = 180.00   # Industry Average Total Debt, e.g., $180 million
industry_average_total_equity = 170.00  # Industry Average Total Equity, e.g., $170 million

# Calculate Debt to Equity ratio
def calculate_debt_to_equity_ratio(total_debt, total_equity):
    """Calculate the Debt to Equity Ratio."""
    if total_equity == 0:
        raise ValueError("Total equity should not be zero to calculate the Debt to Equity ratio.")
    return total_debt / total_equity

# Calculate Debt to Equity for the company and the industry
de_ratio_company = calculate_debt_to_equity_ratio(company_total_debt, company_total_equity)
de_ratio_industry = calculate_debt_to_equity_ratio(industry_average_total_debt, industry_average_total_equity)

print(f"Company's Debt to Equity Ratio: {de_ratio_company:.2f}")
print(f"Industry Average Debt to Equity Ratio: {de_ratio_industry:.2f}\n")

# Interpretation
if de_ratio_company < de_ratio_industry:
    print("The company has a Debt to Equity ratio below the industry average, indicating potentially lower financial risk compared to industry peers.")
    print("\nFactors and Scenarios Affecting the Ratio:")
    print("1. Strong Cash Flows: May indicate ability to service debt efficiently.")
    print("2. High Reserves: Lower dependence on external debt.")
    print("3. Conservative Financing Strategy: Prioritizes equity over debt.")
else:
    print("The company's Debt to Equity ratio is above the industry average, suggesting a potentially higher financial risk compared to industry peers.")
    print("\nFactors and Scenarios Affecting the Ratio:")
    print("1. Aggressive Expansion: Might be taking on debt for growth.")
    print("2. Market Volatility: High debt could be problematic in a downturn.")
    print("3. Interest Rate Sensitivity: Higher costs if interest rates rise.")
    