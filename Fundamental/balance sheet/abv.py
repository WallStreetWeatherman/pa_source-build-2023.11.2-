# Asset-Based Valuation
#
# Overview:
# The Asset-Based Valuation approach focuses on a company's net asset value, 
# emphasizing the assets and liabilities from the balance sheet. It's particularly 
# useful for companies that have a significant amount of assets compared to earnings.
#
# Desired Value:
# A high net asset value (relative to the market value or share price) might indicate 
# that the company is undervalued. Conversely, if the net asset value is much lower 
# than the market value, it could suggest overvaluation.

def asset_based_valuation(current_assets, long_term_assets, liabilities):
    """
    Determine the net asset value of a company.
    
    Parameters:
    - current_assets: Current assets of the company.
    - long_term_assets: Long-term assets of the company.
    - liabilities: Total liabilities of the company.
    
    Returns:
    - Net asset value of the company.
    """
    return (current_assets + long_term_assets) - liabilities

# Hardcoded values for the company
current_assets_company = 5.00  # Current assets of the company ($5,000,000)
long_term_assets_company = 8.00  # Long-term assets of the company ($8,000,000)
liabilities_company = 4.50  # Total liabilities of the company ($4,500,000)

# Hardcoded values for industry average
current_assets_industry = 6.00  # Example value
long_term_assets_industry = 7.50  # Example value
liabilities_industry = 4.00  # Example value

net_asset_value_company = asset_based_valuation(current_assets_company, long_term_assets_company, liabilities_company)
net_asset_value_industry = asset_based_valuation(current_assets_industry, long_term_assets_industry, liabilities_industry)

print(f"The net asset value of the company is ${net_asset_value_company} million.")
print(f"The average net asset value in the industry is ${net_asset_value_industry} million.\n")

# Interpretation
if net_asset_value_company > net_asset_value_industry:
    print("The company has a higher net asset value than the industry average, suggesting it might be undervalued.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Underappreciated Assets: The market may not yet have fully recognized the value of the company's assets.")
    print("2. Low Debt: Lower liabilities relative to assets may indicate a healthier financial position.")
elif net_asset_value_company < net_asset_value_industry:
    print("The company has a lower net asset value than the industry average, suggesting potential overvaluation.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Overvaluation: Market perception might be overly optimistic, driving the share price higher than asset value.")
    print("2. Asset Efficiency: The company may not be utilizing its assets as effectively as peers.")
else:
    print("The company's net asset value is on par with the industry average.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Market Alignment: The company's assets and liabilities are balanced relative to industry norms.")
    print("2. Stable Position: No significant competitive advantages or disadvantages from an asset-based perspective.")
    