# Defensive Interval Ratio Calculator with Industry Comparison
# -----------------------------------------------------------
# Overview:
# The Defensive Interval Ratio provides insight into how many days a company can run its operations without 
# depending on non-core revenue or external financing. This script also contrasts the firm's ratio with 
# the industry average to assess its position relative to its competitors.
#
# Formula:
# Defensive Interval Ratio = Quick Assets / Daily Operational Expenses
#
# Where,
# Quick Assets = Current Assets - Inventory - Prepaid Expenses
# Daily Operational Expenses = (Annual Operational Expenses) / 365
#
# Desired Value:
# A higher Defensive Interval Ratio suggests the company can function for a more extended period without 
# relying on non-core capital sources. A lower ratio might signal short-term liquidity challenges.
# Comparing with the industry average offers contextual insight.
#
# Note: This script uses hard-coded values for illustration. For real-world applications, 
# actual financial data values should be input.

def convert_to_actual_value(value_in_millions):
    """Convert values where 1 million dollars is shown as 1.00, 10 million as 10.00, etc."""
    return value_in_millions * 1000000

# Company's hard-coded values
current_assets_in_millions = 16304.00  
current_assets = convert_to_actual_value(current_assets_in_millions)

inventory_in_millions = 4128.00  
inventory = convert_to_actual_value(inventory_in_millions)

prepaid_expenses_in_millions = 317.00  
prepaid_expenses = convert_to_actual_value(prepaid_expenses_in_millions)

annual_operational_expenses_in_millions = 8377.00  
annual_operational_expenses = convert_to_actual_value(annual_operational_expenses_in_millions)

# Industry average hard-coded values
industry_avg_current_assets_in_millions = 15000.00  # Example value
industry_avg_current_assets = convert_to_actual_value(industry_avg_current_assets_in_millions)

industry_avg_inventory_in_millions = 4000.00  # Example value
industry_avg_inventory = convert_to_actual_value(industry_avg_inventory_in_millions)

industry_avg_prepaid_expenses_in_millions = 300.00  # Example value
industry_avg_prepaid_expenses = convert_to_actual_value(industry_avg_prepaid_expenses_in_millions)

industry_avg_annual_operational_expenses_in_millions = 8000.00  # Example value
industry_avg_annual_operational_expenses = convert_to_actual_value(industry_avg_annual_operational_expenses_in_millions)

# Calculate Defensive Interval Ratios
company_quick_assets = current_assets - inventory - prepaid_expenses
industry_avg_quick_assets = industry_avg_current_assets - industry_avg_inventory - industry_avg_prepaid_expenses

company_daily_operational_expenses = annual_operational_expenses / 365
industry_avg_daily_operational_expenses = industry_avg_annual_operational_expenses / 365

company_ratio = company_quick_assets / company_daily_operational_expenses
industry_avg_ratio = industry_avg_quick_assets / industry_avg_daily_operational_expenses

# Output the results
print(f"Company's Defensive Interval Ratio: {company_ratio:.2f} days")
print(f"Industry Average Defensive Interval Ratio: {industry_avg_ratio:.2f} days")

if company_ratio > industry_avg_ratio:
    print("The company's Defensive Interval Ratio surpasses the industry average, implying a better short-term liquidity position compared to peers.")
    print("\nFactors and Scenarios Affecting the Ratio:")
    print("1. Effective Inventory Management: Lower inventory levels contributing to higher quick assets.")
    print("2. Low Operational Costs: A lower daily operational cost elevates the ratio.")
    print("3. Robust Receivables: Higher amounts of collectible accounts receivable.")
else:
    print("The company's Defensive Interval Ratio is below the industry average, signaling potential liquidity concerns in relation to the industry.")
    print("\nFactors and Scenarios Affecting the Ratio:")
    print("1. High Inventory Levels: Tying up more assets in inventory, reducing quick assets.")
    print("2. Rising Operational Costs: Increasing the daily costs, affecting the ratio negatively.")
    print("3. Poor Cash Management: Lower levels of cash or equivalents can reduce the ratio.")
    