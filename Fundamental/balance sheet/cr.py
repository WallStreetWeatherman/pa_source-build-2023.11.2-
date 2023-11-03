# Capitalization Ratio Calculator with Industry Comparison
# --------------------------------------------------------
# Overview:
# The Capitalization Ratio assesses a company's financial leverage by comparing total equity 
# to total capital (sum of debt and equity). This script also compares the calculated ratio 
# with the industry average to gauge the company's position relative to its peers.
#
# Formula:
# Capitalization Ratio = Total Equity / (Total Debt + Total Equity)
#
# Desired Value:
# A high Capitalization Ratio suggests that the company relies more on equity than debt for its funding,
# indicating a safer financial position. Conversely, a low ratio might show higher leverage and potential financial risk.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

def convert_to_actual_value(value_in_millions):
    """Convert value where 1 million dollars is represented as 1.00, 10 million as 10.00, etc."""
    return value_in_millions * 1000000

# Hard-coded values for the company
company_total_equity_in_millions = 4210.00 # Total Equity in Tikr
company_total_equity = convert_to_actual_value(company_total_equity_in_millions)

company_total_debt_in_millions = 5972.00 # Total Debt in Tikr6
company_total_debt = convert_to_actual_value(company_total_debt_in_millions)

# Industry averages
industry_avg_equity_in_millions = 4000.00  
industry_avg_equity = convert_to_actual_value(industry_avg_equity_in_millions)

industry_avg_debt_in_millions = 6000.00  
industry_avg_debt = convert_to_actual_value(industry_avg_debt_in_millions)

# Calculate Capitalization Ratios
company_ratio = company_total_equity / (company_total_debt + company_total_equity)
industry_avg_ratio = industry_avg_equity / (industry_avg_debt + industry_avg_equity)

# Output the results
print(f"Company's Capitalization Ratio: {company_ratio:.2f}")
print(f"Industry Average Capitalization Ratio: {industry_avg_ratio:.2f}")

if company_ratio > industry_avg_ratio:
    print("The company's Capitalization Ratio is higher than the industry average, suggesting a stronger reliance on equity for funding.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Strong Retained Earnings: The company might have robust profits that are reinvested, boosting equity.")
    print("2. Lower Debt Issuance: The company may be cautious about borrowing, leading to less debt.")
    print("3. Equity Infusion: There might have been an equity investment recently that increased total equity.")
else:
    print("The company's Capitalization Ratio is below the industry average, indicating potential higher leverage and financial risk.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. High Debt Financing: The company may have borrowed significantly for operations or acquisitions.")
    print("2. Share Buybacks: The reduction in equity can tilt the balance towards debt.")
    print("3. Financial Distress: Prolonged operational inefficiencies could erode equity.")
    