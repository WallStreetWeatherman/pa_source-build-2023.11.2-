# Capital Invested Calculator
# -------------------------------------------------
# Overview:
# Capital Invested represents the total amount of money that shareholders and debtholders have provided for company operations.
# It provides an understanding of the resources the company has been entrusted with by its stakeholders.
#
# Formula:
# Capital Invested = Total Assets - Current Liabilities
#
# Desired Value:
# The "Capital Invested" doesn't inherently have a "desired" value (like high or low). Instead, it's used as an input 
# to many other financial metrics to gauge profitability, efficiency, and ROI. Typically, a profitable company will 
# see growth in capital over time due to retained earnings and potential additional investments.
#
# Industry Average:
# Comparing "Capital Invested" with industry averages can give a perspective of the company's relative size and market position.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company
total_assets_in_millions = 1000.00  # Total Assets in Tikr
current_liabilities_in_millions = 200.00  # This would be equivalent to $200 million.

total_assets = convert_to_actual_value(total_assets_in_millions)
current_liabilities = convert_to_actual_value(current_liabilities_in_millions)

# Calculate Capital Invested for the company
capital_invested = total_assets - current_liabilities

# Hard-coded values for the industry average
industry_avg_total_assets_in_millions = 1200.00  # This would be equivalent to $1.2 billion.
industry_avg_current_liabilities_in_millions = 250.00  # This would be equivalent to $250 million.

industry_avg_total_assets = convert_to_actual_value(industry_avg_total_assets_in_millions)
industry_avg_current_liabilities = convert_to_actual_value(industry_avg_current_liabilities_in_millions)

# Calculate Industry Average Capital Invested
industry_avg_capital_invested = industry_avg_total_assets - industry_avg_current_liabilities

# Output the results
print(f"Company's Capital Invested: ${capital_invested:,.2f}")
print(f"Industry Average Capital Invested: ${industry_avg_capital_invested:,.2f}")

# Analysis based on comparison with industry average
if capital_invested > industry_avg_capital_invested:
    print("The company has a higher capital invested than the industry average, indicating a potential market leadership or higher scale of operations.")
    print("Factors and Scenarios Affecting Capital Invested:")
    print("1. Higher Asset Base: The company could have more assets, either in the form of property, plant, and equipment or intellectual property.")
    print("2. Retained Earnings: Sufficient profitability retained in the business can also elevate capital invested.")
    print("3. External Funding: The company may have successfully raised funds through debt or equity to finance its operations.")
else:
    print("The company has a capital invested below the industry average. It's essential to understand if this is due to operational efficiency or smaller scale.")
    print("Factors and Scenarios Affecting Capital Invested:")
    print("1. Asset Light Model: The company may operate an asset-light business model requiring fewer assets.")
    print("2. Operational Efficiency: Efficient management of resources can also lead to less capital being tied up.")
    print("3. Recent Divestitures: The sale of business units or assets can temporarily or permanently reduce the capital invested.")
    