# Projected WACC and ROIC Calculator
# -----------------------------------
# Overview:
# This script projects future WACC (Weighted Average Cost of Capital) and ROIC 
# (Return on Invested Capital) for a given company. Both metrics are essential 
# in determining a company's potential profitability and investment attractiveness.
#
# Desired Value:
# A higher projected ROIC and a lower projected WACC are generally favorable, 
# as a high ROIC indicates efficient capital usage, and a low WACC indicates 
# cheaper cost of capital.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def project_wacc(equity_cost, debt_cost, equity_ratio, debt_ratio, tax_rate):
    """Calculates projected WACC based on given parameters."""
    return (equity_cost * equity_ratio) + (debt_cost * debt_ratio * (1 - tax_rate))

def project_roic(operating_income, invested_capital, tax_rate):
    """Calculates projected ROIC based on given parameters."""
    return (operating_income * (1 - tax_rate)) / invested_capital

# Hardcoded values for the company
equity_cost_company = 0.10  # Cost of equity
debt_cost_company = 0.04  # Cost of debt
equity_ratio_company = 0.6  # Equity to total capital ratio
debt_ratio_company = 0.4  # Debt to total capital ratio
tax_rate = 0.2  # Corporate tax rate (assumed to be same for industry)
operating_income_company = convert_to_actual_value(150.00)  # Operating income
invested_capital_company = convert_to_actual_value(1200.00)  # Invested capital

# Hardcoded values for industry average
equity_cost_industry = 0.09  # Example value
debt_cost_industry = 0.05  # Example value
equity_ratio_industry = 0.55  # Example value
debt_ratio_industry = 0.45  # Example value
operating_income_industry = convert_to_actual_value(140.00)  # Example value
invested_capital_industry = convert_to_actual_value(1100.00)  # Example value

# Project WACC and ROIC for the company and industry
projected_wacc_company = project_wacc(equity_cost_company, debt_cost_company, equity_ratio_company, debt_ratio_company, tax_rate)
projected_roic_company = project_roic(operating_income_company, invested_capital_company, tax_rate)

projected_wacc_industry = project_wacc(equity_cost_industry, debt_cost_industry, equity_ratio_industry, debt_ratio_industry, tax_rate)
projected_roic_industry = project_roic(operating_income_industry, invested_capital_industry, tax_rate)

# Output the results
print(f"Company's Projected WACC: {projected_wacc_company:.4f} or {projected_wacc_company * 100:.2f}%")
print(f"Industry Average Projected WACC: {projected_wacc_industry:.4f} or {projected_wacc_industry * 100:.2f}%\n")

print(f"Company's Projected ROIC: {projected_roic_company:.4f} or {projected_roic_company * 100:.2f}%")
print(f"Industry Average Projected ROIC: {projected_roic_industry:.4f} or {projected_roic_industry * 100:.2f}%\n")

print("\nFactors and Scenarios potentially influencing the metrics:")
print("- Interest Rate Environment: The cost of debt can be influenced by the prevailing interest rates. A rising rate environment can increase the WACC, making it costlier for firms to finance projects.")
print("- Market Conditions: Market optimism or pessimism can impact the cost of equity. During bullish conditions, investors might demand lower returns, reducing the equity cost.")
print(f"- Company's Financial Health: With an equity cost of {equity_cost_company * 100:.2f}% and debt cost of {debt_cost_company * 100:.2f}%, the company's financial structure and health can be a determinant. High debt levels, for instance, might increase the perceived risk and thus the cost of capital.")
print("- Industry Dynamics: Capital-intensive industries or those with cyclical operations might have varying WACC and ROIC figures compared to more stable industries.")
print("- Operational Efficiency: The ROIC is influenced by how efficiently a company utilizes its capital. Operational inefficiencies, outdated technology, or unproductive assets can depress ROIC.")

print("\nImplications:")
if projected_roic_company > projected_wacc_company:
    print("The company is expected to generate a return greater than its cost of capital, which is generally favorable. Such companies might be better positioned to create value for shareholders.")
else:
    print("The company is not expected to generate a return greater than its cost of capital, indicating potential challenges in value creation. Investors should be cautious and delve deeper into the company's operations and strategies.")
    
if projected_roic_company > projected_roic_industry:
    print("The company's projected ROIC is above the industry average, hinting at potential outperformance. This could be due to superior management, competitive advantages, or innovative strategies.")
elif projected_roic_company < projected_roic_industry:
    print("The company's projected ROIC is below the industry average. This might be due to operational challenges, tougher competition, or less efficient capital usage. It's worth investigating further.")
else:
    print("The company's projected ROIC aligns with the industry average, suggesting it operates at par with its peers.")
