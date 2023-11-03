# DuPont Analysis Calculator
# ---------------------------
# Overview:
# The DuPont Analysis decomposes the Return on Equity (ROE) into its influencing factors.
# It is a fundamental tool for assessing the quality of a company's earnings by gauging 
# the relative contributions of its profit margin, asset turnover, and financial leverage.
# 
# Formula:
# ROE = (Net Profit Margin) * (Asset Turnover) * (Equity Multiplier)
# 
# Desired Value:
# A higher ROE is generally more desirable, provided it is achieved through a higher profit 
# margin and asset turnover rather than excessive financial leverage.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# financial statement data should be input.

# Representing financial values in millions as decimals
net_income = 5.00  # Represents $5 million
sales = 50.00  # Represents $50 million
total_assets = 100.00  # Represents $100 million
shareholders_equity = 25.00  # Represents $25 million

# Calculating the three components of the DuPont Analysis
net_profit_margin = net_income / sales
asset_turnover = sales / total_assets
equity_multiplier = total_assets / shareholders_equity

# Calculating ROE using the DuPont Analysis
roe = net_profit_margin * asset_turnover * equity_multiplier

# Outputting the results
print(f"Net Profit Margin: {net_profit_margin:.2%}")
print(f"Asset Turnover: {asset_turnover:.2f}")
print(f"Equity Multiplier: {equity_multiplier:.2f}")
print(f"Return on Equity (ROE): {roe:.2%}")
