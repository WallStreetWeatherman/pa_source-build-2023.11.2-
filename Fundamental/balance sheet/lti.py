# Long-Term Investment Approach Calculator
# ----------------------------------------
# Overview:
# The Long-Term Investment Approach evaluates a company's long-term assets and working capital to gauge its 
# long-term investment strategy. A higher long-term investment value can indicate a company's commitment to 
# future growth, while a lower value might indicate a more short-term operational focus.
#
# Formula:
# Long-Term Investments = Long-Term Assets + Working Capital
# Working Capital = Current Assets - Current Liabilities
#
# Desired Value:
# There's no definitive 'right' value for long-term investments. The value should be analyzed in the context 
# of the industry, company's stage of development, and its overall strategy.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Long-Term Assets (in million dollars format for simplicity)
long_term_assets_in_millions = 15000.00
long_term_assets = convert_to_actual_value(long_term_assets_in_millions)

# Current Assets (in million dollars format for simplicity)
current_assets_in_millions = 5000.00
current_assets = convert_to_actual_value(current_assets_in_millions)

# Current Liabilities (in million dollars format for simplicity)
current_liabilities_in_millions = 3000.00
current_liabilities = convert_to_actual_value(current_liabilities_in_millions)

# Hard-coded values for industry average

# Industry Average Long-Term Assets (in million dollars format for simplicity)
industry_avg_long_term_assets_in_millions = 14500.00
industry_avg_long_term_assets = convert_to_actual_value(industry_avg_long_term_assets_in_millions)

# Industry Average Current Assets (in million dollars format for simplicity)
industry_avg_current_assets_in_millions = 4800.00
industry_avg_current_assets = convert_to_actual_value(industry_avg_current_assets_in_millions)

# Industry Average Current Liabilities (in million dollars format for simplicity)
industry_avg_current_liabilities_in_millions = 2900.00
industry_avg_current_liabilities = convert_to_actual_value(industry_avg_current_liabilities_in_millions)

# Calculate Long-Term Investments for the company and industry average
working_capital = current_assets - current_liabilities
industry_avg_working_capital = industry_avg_current_assets - industry_avg_current_liabilities

long_term_investments = long_term_assets + working_capital
industry_avg_long_term_investments = industry_avg_long_term_assets + industry_avg_working_capital

# Convert back to millions for easier readability
long_term_investments_in_millions = long_term_investments / 1000000
industry_avg_long_term_investments_in_millions = industry_avg_long_term_investments / 1000000

# Output the results
print(f"Company's Long-Term Investments: ${long_term_investments_in_millions:.2f} million")
print(f"Industry Average Long-Term Investments: ${industry_avg_long_term_investments_in_millions:.2f} million")

# Interpretation and Discussing Influencing Factors
if long_term_investments_in_millions > industry_avg_long_term_investments_in_millions:
    print("\nThe company has more Long-Term Investments than the industry average. Influencing factors might include:")
    print("1. A strategic focus on R&D, hinting at innovation and long-term growth.")
    print("2. Strong working capital management, potentially due to efficient inventory turnover or robust accounts receivable.")
    print("3. A diverse asset portfolio, suggesting the company is hedging against specific market risks.")
    
elif long_term_investments_in_millions == industry_avg_long_term_investments_in_millions:
    print("\nThe company's Long-Term Investments align with the industry average. Influencing scenarios could be:")
    print("1. The company is adhering to industry standards in asset allocation.")
    print("2. Possible market maturity, where the company and industry are stable and thus exhibit similar financial behavior.")
    
else:
    print("\nThe company has fewer Long-Term Investments than the industry average. Possible reasons include:")
    print("1. A focus on short-term liquidity, perhaps due to market volatility or operational necessities.")
    print("2. An industry-disruptive approach, where the company may be investing in non-traditional assets not reflected in 'Long-Term Assets'.")
    print("3. Recent divestitures or asset sales, which would reduce the long-term asset base but might be aimed at business refocusing.")
    