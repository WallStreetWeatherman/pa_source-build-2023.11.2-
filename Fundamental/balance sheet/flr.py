# Financial Leverage Ratio Calculator
# -----------------------------------
# Overview:
# The Financial Leverage Ratio evaluates the proportion of total assets financed by shareholders 
# compared to total assets financed by creditors. It provides insight into the company's capital structure.
#
# Formula:
# Financial Leverage Ratio = Total Assets / Shareholder's Equity
#
# Desired Value:
# A high Financial Leverage Ratio indicates that a significant portion of the company's assets are financed by debt, 
# which may pose greater financial risk, especially during downturns. Conversely, a low ratio suggests that a 
# company is relying less on external creditors and more on equity financing. Optimal ratios may vary across industries.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Total Assets (in million dollars format for simplicity)
company_total_assets_in_millions = 16304.00
company_total_assets = convert_to_actual_value(company_total_assets_in_millions)

# Shareholder's Equity (in million dollars format for simplicity)
company_shareholders_equity_in_millions = 4210.00
company_shareholders_equity = convert_to_actual_value(company_shareholders_equity_in_millions)

# Hard-coded values for the industry average

# Total Assets
industry_average_total_assets_in_millions = 15000.00  # Placeholder value
industry_average_total_assets = convert_to_actual_value(industry_average_total_assets_in_millions)

# Shareholder's Equity
industry_average_shareholders_equity_in_millions = 4000.00  # Placeholder value
industry_average_shareholders_equity = convert_to_actual_value(industry_average_shareholders_equity_in_millions)

# Calculate Financial Leverage Ratios
company_financial_leverage_ratio = company_total_assets / company_shareholders_equity
industry_average_financial_leverage_ratio = industry_average_total_assets / industry_average_shareholders_equity

# Output the results
print(f"Company Total Assets: ${company_total_assets_in_millions} million")
print(f"Company Shareholder's Equity: ${company_shareholders_equity_in_millions} million")
print(f"Company Financial Leverage Ratio: {company_financial_leverage_ratio:.2f}")

print(f"\nIndustry Average Total Assets: ${industry_average_total_assets_in_millions} million")
print(f"Industry Average Shareholder's Equity: ${industry_average_shareholders_equity_in_millions} million")
print(f"Industry Average Financial Leverage Ratio: {industry_average_financial_leverage_ratio:.2f}")

# Factors and Scenarios Affecting the Financial Leverage Ratio
print("\n---------- Factors and Scenarios Affecting the Financial Leverage Ratio ----------")

print("\n1. Interest Rates:")
print("   - Lower interest rates could encourage more debt financing, increasing the ratio.")
print("   - Higher interest rates may deter debt financing, potentially lowering the ratio.")

print("\n2. Business Cycle:")
print("   - During a boom, companies may take on more debt due to optimism, affecting the ratio.")
print("   - During downturns, companies may reduce debt, affecting the ratio.")

print("\n3. Company Life Stage:")
print("   - Startups or growth-stage companies may have higher leverage to finance rapid growth.")
print("   - Mature companies may have lower leverage, relying more on internally generated funds.")

print("\n4. Industry Norms:")
print("   - Some industries naturally have higher leverage due to capital requirements.")
print("   - Compare with industry averages to understand relative risk.")

print("\n5. Asset Structure:")
print("   - A high proportion of fixed assets may justify a higher leverage ratio.")
print("   - Companies with more liquid assets may opt for lower leverage.")

# Compare company's Financial Leverage Ratio with industry average
if company_financial_leverage_ratio > industry_average_financial_leverage_ratio:
    print("\nThe company has higher financial leverage than the industry average, indicating potential higher financial risk.")
elif company_financial_leverage_ratio < industry_average_financial_leverage_ratio:
    print("\nThe company has lower financial leverage than the industry average, indicating potential lower financial risk.")
else:
    print("\nThe company's financial leverage is in line with the industry average.")