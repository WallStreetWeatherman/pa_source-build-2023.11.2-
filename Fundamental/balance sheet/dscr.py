# Debt Service Coverage Ratio (DSCR) Calculator with Industry Comparison
# ----------------------------------------------------------------------
# Overview:
# The Debt Service Coverage Ratio (DSCR) evaluates a company's capacity to cover its 
# debt commitments, shedding light on its financial robustness and default risk.
#
# Formula:
# DSCR = Net Operating Income / Total Debt Service
# Where,
# Total Debt Service = Total Debt Repaid + Interest Expense
#
# Desired Value:
# A DSCR higher than 1 implies that the company has adequate income to fulfill its 
# debt obligations. A ratio below 1, however, indicates potential liquidity problems 
# and a heightened risk of default.

# Hard-coded company values (in millions as decimals)
company_net_operating_income = 15269.00  # e.g., $15 million
company_total_debt_service = 2164.00  # e.g., $10 million debt obligations

# Industry average hard-coded values (in millions as decimals)
industry_avg_net_operating_income = 14000.00  # Example value
industry_avg_total_debt_service = 2000.00  # Example value

# Calculate company's DSCR
company_dscr = company_net_operating_income / company_total_debt_service if company_total_debt_service != 0 else float('inf')

# Calculate industry average DSCR
industry_dscr = industry_avg_net_operating_income / industry_avg_total_debt_service if industry_avg_total_debt_service != 0 else float('inf')

# Output the results and comparison
print(f"Company's Net Operating Income (in $1M): ${company_net_operating_income:.2f}M")
print(f"Company's Total Debt Service (in $1M): ${company_total_debt_service:.2f}M")
print(f"Company's Debt Service Coverage Ratio (DSCR): {company_dscr:.2f}\n")

print(f"Industry Average Net Operating Income (in $1M): ${industry_avg_net_operating_income:.2f}M")
print(f"Industry Average Total Debt Service (in $1M): ${industry_avg_total_debt_service:.2f}M")
print(f"Industry Average Debt Service Coverage Ratio (DSCR): {industry_dscr:.2f}\n")

if company_dscr > industry_dscr:
    print(f"The company's DSCR of {company_dscr:.2f} is above the industry average of {industry_dscr}. This suggests a robust position in handling its debt obligations compared to peers.")
    print("\nFactors and Scenarios Affecting the Ratio:")
    print("1. Solid Revenue Streams: Could imply a greater ability to manage debt.")
    print("2. Effective Cost Management: Lower operating expenses lead to higher NOI.")
    print("3. Favorable Market Conditions: Strong demand for products or services.")
elif company_dscr == industry_dscr:
    print(f"The company's DSCR of {company_dscr:.2f} matches the industry average of {industry_dscr}. It's on par with industry standards.")
    print("\nFactors and Scenarios Affecting the Ratio:")
    print("1. Average Market Performance: Neither excelling nor lagging in revenue.")
    print("2. Moderate Leverage: The company is not overburdened by debt.")
else:
    print(f"The company's DSCR of {company_dscr:.2f} is below the industry average of {industry_dscr}. This indicates potential challenges relative to industry standards.")
    print("\nFactors and Scenarios Affecting the Ratio:")
    print("1. Reduced Revenue: Lower sales affecting ability to service debt.")
    print("2. Increased Operating Costs: Higher costs affecting net operating income.")
    print("3. Market Competition: Losing market share to competitors.")