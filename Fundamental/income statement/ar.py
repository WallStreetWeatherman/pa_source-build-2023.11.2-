# Accruals Ratio Calculator
# -------------------------
# Overview:
# The Accruals Ratio helps assess the quality of a company's earnings by comparing the difference between net income 
# and operating cash flow relative to total assets. A higher ratio can signal aggressive accounting practices, 
# such as prematurely recognizing revenue or delaying expense recognition.
#
# Formula:
# Accruals Ratio = (Net Income - Operating Cash Flow) / Total Assets
#
# Desired Value:
# Ideally, the Accruals Ratio should be low, as this would indicate that most of the company's earnings are backed 
# by actual cash flows. A high Accruals Ratio can be a red flag, signaling that earnings might not be as reliable or sustainable.

# Net Income for the period (in $1M)
net_income = 1177.00  # Net Income in Tikr

# Operating Cash Flow for the period (in $1M)
operating_cash_flow = 1615.00  # Cash from Operations in Tikr

# Total Assets (in $1M)
total_assets = 16866.00  # Total Assest in Tikr

# Industry Average values (hypothetical for this example)
industry_avg_net_income = 324.00
industry_avg_operating_cash_flow = 803.00
industry_avg_total_assets = 7390.00

# Calculate Accruals Ratio
def calculate_accruals_ratio(net_income, operating_cash_flow, total_assets):
    """Calculate Accruals Ratio."""
    return (net_income - operating_cash_flow) / total_assets

company_accruals_ratio = calculate_accruals_ratio(net_income, operating_cash_flow, total_assets)
industry_accruals_ratio = calculate_accruals_ratio(industry_avg_net_income, industry_avg_operating_cash_flow, industry_avg_total_assets)

print(f"Company's Accruals Ratio: {company_accruals_ratio:.2%}")
print(f"Industry Average Accruals Ratio: {industry_accruals_ratio:.2%}")

print("\nFactors and Scenarios Influencing Accruals Ratio:")
print("- **Accounting Choices:** The adoption of certain accounting methods over others, like FIFO vs. LIFO or straight-line vs. declining balance depreciation, can impact the ratio.")
print("- **Business Cycles:** Seasonal or cyclical businesses might see variations in their accruals ratio due to timing differences in revenue and expense recognition.")
print("- **Cash Flow Volatility:** Erratic cash flows can skew the ratio, especially if there are significant one-off transactions.")
print("- **Capital Expenditures:** High capital expenses might lead to a rise in depreciation, affecting both net income and operating cash flow.")
print("- **Revenue Recognition:** Companies recognizing revenue aggressively can have higher accruals, which might elevate the ratio.")
print("- **Expense Management:** Delaying expense recognition or capitalizing certain costs can also drive up the ratio.")

print("\nComparative Analysis:")
if company_accruals_ratio > industry_accruals_ratio:
    print("The company's Accruals Ratio is above the industry benchmark. This might be a sign of aggressive accounting practices, warranting further scrutiny.")
elif company_accruals_ratio == industry_accruals_ratio:
    print("The company's Accruals Ratio matches the industry average. It's still essential to assess other financial indicators for a holistic view.")
else:
    print("The company's Accruals Ratio is below the industry mean, hinting at potentially higher earnings quality and reliability.")
