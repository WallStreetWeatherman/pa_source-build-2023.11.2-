# Operating Cash Flow Calculator
# ------------------------------
# Overview:
# The Operating Cash Flow (OCF) indicates the cash generated from the core operations of a business.
# It serves as a key indicator of the health and profitability of a business's primary activities.
#
# Formula:
# Operating Cash Flow (OCF) = Earnings Before Interest and Taxes (EBIT) + Depreciation - Taxes - Change in Working Capital
#
# Note: The change in working capital is the difference between current assets and current liabilities 
# from one period to the next.
#
# Desired Value:
# A positive OCF suggests that the company is generating enough cash from its core operations to maintain 
# and grow the business. A negative OCF may indicate challenges in the company's primary operational profitability.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Earnings Before Interest and Taxes (EBIT) (in million dollars format for simplicity)
ebit_in_millions = 451.00  
ebit = convert_to_actual_value(ebit_in_millions)

# Depreciation (in million dollars format for simplicity)
depreciation_in_millions = 620.00  
depreciation = convert_to_actual_value(depreciation_in_millions)

# Taxes (in million dollars format for simplicity)
taxes_in_millions = 365.00  # 'cash taxes paid' in tikr
taxes = convert_to_actual_value(taxes_in_millions)

# Change in Working Capital (in million dollars format for simplicity)
change_in_working_capital_in_millions = -208.00  # Example value representing a decrease of 1 million dollars
change_in_working_capital = convert_to_actual_value(change_in_working_capital_in_millions)

# Calculate Operating Cash Flow
ocf = ebit + depreciation - taxes - change_in_working_capital

# Output the results
print(f"Operating Cash Flow (OCF): ${ocf/1000000:.2f} million\n")

# Delving into components and potential influencing factors
print("Breaking down the components and potential influencing factors:")
print(f"Earnings Before Interest and Taxes (EBIT): ${ebit_in_millions:.2f} million")
if ebit > 0:
    print("- A positive EBIT indicates operational profitability. Influencing factors might include strong sales, cost control measures, and efficient operations.")
else:
    print("- A negative EBIT indicates operational challenges, potentially due to declining sales, high operational costs, or external economic factors.")

print(f"Depreciation: ${depreciation_in_millions:.2f} million")
print("- Depreciation is a non-cash expense, which gets added back to cash flow. A high depreciation value could indicate significant investments in fixed assets in previous years or the use of accelerated depreciation methods.")

print(f"Taxes Paid: ${taxes_in_millions:.2f} million")
print("- Taxes represent cash outflows. Factors influencing tax amounts can include changes in tax laws, credits or deductions the company can claim, or deferred tax strategies.")

print(f"Change in Working Capital: ${change_in_working_capital_in_millions:.2f} million")
if change_in_working_capital < 0:
    print("- A negative change in working capital implies an increase in current assets or a decrease in current liabilities. This might be due to increased sales (leading to higher accounts receivables) or efficient management of short-term debts.")
else:
    print("- A positive change in working capital suggests a decrease in current assets or an increase in current liabilities, potentially indicating liquidity concerns or slower sales.")

print("\nOverall Insights:")
if ocf > 0:
    print("The company is generating a positive cash flow from its core operations. This is a healthy sign, indicating the business can sustain and potentially expand its operations.")
else:
    print("The company is facing challenges in generating cash from its core operations. Investigating the specific components can give insights into areas needing attention.")
