# Liquidity Index Calculator
# --------------------------
# Overview:
# The Liquidity Index measures the availability of liquid assets to cover current liabilities.
# It's a ratio that provides insights into a company's short-term solvency and financial health.
#
# Formula:
# Liquidity Index = (Current Assets - Inventory) / Current Liabilities
#
# Desired Value:
# A Liquidity Index greater than 1 suggests that the company has enough liquid assets 
# to cover its short-term obligations. A value below 1 might indicate potential liquidity concerns.
# It's important to compare this metric with industry benchmarks for a comprehensive understanding.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Current Assets
company_current_assets_in_millions = 5271.00
company_current_assets = convert_to_actual_value(company_current_assets_in_millions)

# Inventory
company_inventory_in_millions = 4129.00
company_inventory = convert_to_actual_value(company_inventory_in_millions)

# Current Liabilities
company_current_liabilities_in_millions = 4184.00
company_current_liabilities = convert_to_actual_value(company_current_liabilities_in_millions)

# Hard-coded values for the industry average

# Current Assets
industry_average_current_assets_in_millions = 5000.00  # Placeholder value
industry_average_current_assets = convert_to_actual_value(industry_average_current_assets_in_millions)

# Inventory
industry_average_inventory_in_millions = 4000.00  # Placeholder value
industry_average_inventory = convert_to_actual_value(industry_average_inventory_in_millions)

# Current Liabilities
industry_average_current_liabilities_in_millions = 4500.00  # Placeholder value
industry_average_current_liabilities = convert_to_actual_value(industry_average_current_liabilities_in_millions)

# Calculate Liquidity Indexes
company_liquidity_index = (company_current_assets - company_inventory) / company_current_liabilities
industry_average_liquidity_index = (industry_average_current_assets - industry_average_inventory) / industry_average_current_liabilities

# Output the results
print(f"Company Current Assets: ${company_current_assets_in_millions} million")
print(f"Company Inventory: ${company_inventory_in_millions} million")
print(f"Company Current Liabilities: ${company_current_liabilities_in_millions} million")
print(f"Company Liquidity Index: {company_liquidity_index:.2f}")

print(f"\nIndustry Average Current Assets: ${industry_average_current_assets_in_millions} million")
print(f"Industry Average Inventory: ${industry_average_inventory_in_millions} million")
print(f"Industry Average Current Liabilities: ${industry_average_current_liabilities_in_millions} million")
print(f"Industry Average Liquidity Index: {industry_average_liquidity_index:.2f}")

# Discussing Influencing Factors and Scenarios
if company_liquidity_index > industry_average_liquidity_index:
    print("\nThe company's liquidity position is better than the industry average. Possible influencing factors include:")
    print("1. Strong receivables collection, improving liquid assets.")
    print("2. A conservative inventory management strategy, avoiding excessive stockpile.")
    print("3. Short-term debt management, perhaps indicating good creditor relationships.")

elif company_liquidity_index < industry_average_liquidity_index:
    print("\nThe company's liquidity position is weaker than the industry average. Consider these scenarios:")
    print("1. The high inventory level could signify slow-moving stock, affecting liquidity.")
    print("2. Higher current liabilities may indicate a reliance on short-term financing, posing a risk.")
    print("3. The low liquidity could also be seasonal or linked to a specific project, warranting further investigation.")
  
else:
    print("\nThe company's liquidity position is in line with the industry average. Influencing factors could be:")
    print("1. Standard industry practices are closely followed in terms of asset and liability management.")
    print("2. The company is neither an outlier in risk-taking nor in conservatism, suggesting operational stability.")
    