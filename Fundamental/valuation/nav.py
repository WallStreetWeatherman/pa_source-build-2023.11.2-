# Net Asset Value (NAV) Calculator
# --------------------------------
# Overview:
# The Net Asset Value (NAV) is calculated by subtracting the total liabilities from the total assets 
# of a company, and then dividing by the number of shares outstanding. It represents the intrinsic value
# of a company on a per-share basis.
#
# Desired Value:
# Generally, a higher NAV per share indicates a more valuable company. However, it's crucial to compare 
# the NAV with the market value of the shares to determine if the company is overvalued or undervalued.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# financial data should be sourced from the company's balance sheet.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for a hypothetical company
total_assets = convert_to_actual_value(500.00)  # Total Assets in actual value
total_liabilities = convert_to_actual_value(150.00)  # Total Liabilities in actual value
shares_outstanding = 10 * 1000000  # 10 million shares

def calculate_nav(total_assets, total_liabilities, shares_outstanding):
    net_assets = total_assets - total_liabilities
    nav_per_share = net_assets / shares_outstanding
    return nav_per_share

nav_per_share = calculate_nav(total_assets, total_liabilities, shares_outstanding)

# Output the result
print("Net Asset Value (NAV) Calculation:\n")
print("Total Assets: ${:,.2f}".format(total_assets / 1000000))
print("Total Liabilities: ${:,.2f}".format(total_liabilities / 1000000))
print("Shares Outstanding: {:,}".format(shares_outstanding))
print("\nNAV per Share: ${:,.2f}".format(nav_per_share / 1000000))

