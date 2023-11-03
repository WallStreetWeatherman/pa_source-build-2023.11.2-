# Greenblatt's ROC (Return on Capital) Calculation
# ------------------------------------------------
# Overview:
# Greenblatt's ROC measures the return generated on capital employed. It's useful for comparing 
# the relative profitability of companies. The formula used is EBIT / (Net Working Capital + Net Fixed Assets).
#
# Desired Value:
# A higher ROC suggests that the company is using its capital more efficiently to generate profits.
# Comparing ROC values across companies in the same industry can give insights into relative operational efficiency.

# Hardcoded values for the company (in the format where 1 million is represented as 1.00, etc.)
company_ebit = 5.00                # Company's Earnings Before Interest and Taxes (e.g., $5 million)
company_net_working_capital = 2.50 # Company's Net Working Capital (e.g., $2.5 million)
company_net_fixed_assets = 3.00    # Company's Net Fixed Assets (e.g., $3 million)

# Hardcoded industry average values
industry_average_ebit = 45.00               # Industry Average EBIT (e.g., $45 million)
industry_average_net_working_capital = 25.00 # Industry Average Net Working Capital (e.g., $25 million)
industry_average_net_fixed_assets = 30.00    # Industry Average Net Fixed Assets (e.g., $30 million)

# Calculate Greenblatt's ROC
def calculate_greenblatt_roc(ebit, net_working_capital, net_fixed_assets):
    """Calculate Greenblatt's Return on Capital."""
    return ebit / (net_working_capital + net_fixed_assets)

company_roc = calculate_greenblatt_roc(company_ebit, company_net_working_capital, company_net_fixed_assets)
industry_roc = calculate_greenblatt_roc(industry_average_ebit, industry_average_net_working_capital, industry_average_net_fixed_assets)

print(f"Company's Greenblatt's ROC: {company_roc:.2f}")
print(f"Industry Average Greenblatt's ROC: {industry_roc:.2f}\n")

# Interpretation
if company_roc > industry_roc:
    print("The company's ROC is above the industry average, indicating efficient use of capital.")
    print("\nReasons for a higher ROC might include:")
    print("- Better operational efficiencies and management practices.")
    print("- Strategic investments leading to higher returns.")
    print("- Favorable market conditions or proprietary technologies.")
    print("- Efficient working capital management and asset utilization.")
elif company_roc == industry_roc:
    print("The company's ROC is in line with the industry average.")
    print("\nBeing in line suggests that the company is operating at industry norms. It's important to keep monitoring and aim for outperformance.")
else:
    print("The company's ROC is below the industry average, suggesting there might be room for operational improvement.")
    print("\nFactors influencing a lower ROC might include:")
    print("- Sub-optimal use of assets or mismanagement of working capital.")
    print("- Large, recent investments that have yet to generate returns.")
    print("- Declining sales or revenue figures.")
    print("- High operating expenses or inefficiencies in the production process.")
