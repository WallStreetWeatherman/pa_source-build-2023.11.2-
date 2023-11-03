# Quality of Earnings Calculator
# ------------------------------
# Overview:
# The Quality of Earnings metric provides insights into the reliability of a company's reported net income. 
# It compares operating cash flow to net income. A higher ratio indicates that a significant portion of a 
# company's earnings are backed by actual cash inflows, suggesting robust and reliable earnings.
#
# Formula:
# Quality of Earnings = Operating Cash Flow / Net Income
#
# Desired Value:
# A high Quality of Earnings ratio is generally favorable, as it indicates that earnings are backed 
# by actual cash inflows. Conversely, a low ratio can suggest that reported earnings might be influenced 
# by accounting adjustments, non-recurring items, or other factors that don't reflect the company's true operational 
# performance.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# Company's values:
net_income_company = 1177.00  # Net Income in Tikr
operating_cash_flow_company = 1615.00  # Cash from Operations in Tikr

# Industry average values:
net_income_industry = 322.00  
operating_cash_flow_industry = 803.00  

# Calculate Quality of Earnings for the company
quality_of_earnings_company = operating_cash_flow_company / net_income_company

# Calculate Quality of Earnings for the industry average
quality_of_earnings_industry = operating_cash_flow_industry / net_income_industry

# Output the results
print(f"Company's Net Income (in $1M): ${net_income_company:.2f}M")
print(f"Company's Operating Cash Flow (in $1M): ${operating_cash_flow_company:.2f}M")
print(f"Company's Quality of Earnings: {quality_of_earnings_company:.2f}")
print(f"Industry Average Quality of Earnings: {quality_of_earnings_industry:.2f}")

if quality_of_earnings_company > quality_of_earnings_industry:
    print("The company's Quality of Earnings is above the industry average, suggesting more reliable earnings.")
    print("\nFactors potentially contributing to a higher Quality of Earnings include:")
    print("- Strong cash collections from customers, reflecting high-quality revenue.")
    print("- Conservative accounting practices, with fewer accruals or provisions.")
    print("- Minimal non-recurring items or adjustments influencing net income.")
    print("- Effective working capital management leading to consistent cash flow.")

elif quality_of_earnings_company < quality_of_earnings_industry:
    print("The company's Quality of Earnings is below the industry average, suggesting potential discrepancies in reported earnings.")
    print("\nFactors possibly contributing to a lower Quality of Earnings include:")
    print("- Aggressive revenue recognition practices that do not translate into cash collections.")
    print("- Significant non-cash or non-recurring items included in net income.")
    print("- Changes in working capital that tie up cash, such as inventory buildup or delayed payable schedules.")
    print("- Recent major capital expenditures or other operational changes affecting cash flow but not net income.")

else:
    print("The company's Quality of Earnings is in line with the industry average.")
    