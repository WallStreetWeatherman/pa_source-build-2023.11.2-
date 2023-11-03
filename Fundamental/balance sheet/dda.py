# Distressed Debt Analysis
#
# Overview:
# This script calculates key financial metrics to assess the financial health of 
# a company and determine if there might be any value left for equity holders.
#
# Desired Value:
# Higher liquidity ratios (like current ratio) suggest better short-term solvency. 
# A higher debt-to-equity ratio indicates higher financial leverage, increasing the 
# risk for equity holders in distressed scenarios.

# Function to perform the distressed debt analysis
def distressed_debt_analysis(current_assets, current_liabilities, inventory, total_debt, total_equity):
    # Liquidity Ratios
    current_ratio = current_assets / current_liabilities
    quick_ratio = (current_assets - inventory) / current_liabilities

    # Leverage Ratio
    debt_to_equity_ratio = total_debt / total_equity

    return current_ratio, quick_ratio, debt_to_equity_ratio

# Hardcoded values for the company (in the format where 1 million dollars is represented as 1.00)
current_assets = 10.00  # $10 million
current_liabilities = 8.00  # $8 million
inventory = 2.00  # $2 million
total_debt = 15.00  # $15 million
total_equity = 5.00  # $5 million

# Hardcoded industry average values
industry_avg_current_ratio = 1.50
industry_avg_quick_ratio = 1.20
industry_avg_debt_to_equity_ratio = 2.00

current_ratio, quick_ratio, debt_to_equity_ratio = distressed_debt_analysis(current_assets, current_liabilities, inventory, total_debt, total_equity)

# Output the results and interpretations
print(f"Company's Current Ratio: {current_ratio:.2f}")
print(f"Company's Quick Ratio: {quick_ratio:.2f}")
print(f"Company's Debt-to-Equity Ratio: {debt_to_equity_ratio:.2f}\n")

print(f"Industry Average Current Ratio: {industry_avg_current_ratio:.2f}")
print(f"Industry Average Quick Ratio: {industry_avg_quick_ratio:.2f}")
print(f"Industry Average Debt-to-Equity Ratio: {industry_avg_debt_to_equity_ratio:.2f}\n")

# Interpretation
# Comparing company's values with industry averages
if current_ratio >= industry_avg_current_ratio:
    print("The company has a strong Current Ratio compared to the industry average.")
    print("Factors and Scenarios Affecting the Current Ratio:")
    print("1. Efficient Accounts Receivable: Faster collection times improve liquidity.")
    print("2. Conservative Short-Term Borrowing: Lower short-term debt improves the ratio.")
else:
    print("The company's Current Ratio is below the industry average, suggesting potential short-term solvency issues.")
    print("Factors and Scenarios Affecting the Current Ratio:")
    print("1. Liquidity Crunch: Poor working capital management may reduce available cash.")
    print("2. Economic Downturn: Reduced sales and cash inflows could affect the ratio.")

if quick_ratio >= industry_avg_quick_ratio:
    print("\nThe company has a strong Quick Ratio compared to the industry average.")
    print("Factors and Scenarios Affecting the Quick Ratio:")
    print("1. Minimal Inventory: Keeping lower inventory levels can improve the ratio.")
    print("2. High-Quality Investments: Easily liquidated investments contribute to a better quick ratio.")
else:
    print("\nThe company's Quick Ratio is below the industry average, indicating potential liquidity concerns.")
    print("Factors and Scenarios Affecting the Quick Ratio:")
    print("1. Obsolete Inventory: Holding onto outdated inventory can negatively affect liquidity.")
    print("2. Market Volatility: Changes in the value of short-term investments could reduce the ratio.")

if debt_to_equity_ratio <= industry_avg_debt_to_equity_ratio:
    print("\nThe company has a reasonable Debt-to-Equity Ratio compared to the industry average.")
    print("Factors and Scenarios Affecting the Debt-to-Equity Ratio:")
    print("1. Equity Financing: Higher equity financing leads to a lower debt-to-equity ratio.")
    print("2. Asset Sales: Selling non-core assets to pay down debt improves the ratio.")
else:
    print("\nThe company's Debt-to-Equity Ratio is higher than the industry average, suggesting increased financial risk.")
    print("Factors and Scenarios Affecting the Debt-to-Equity Ratio:")
    print("1. Aggressive Borrowing: Higher debt elevates financial risk.")
    print("2. Mergers and Acquisitions: Debt-financed acquisitions can significantly worsen the ratio.")
    