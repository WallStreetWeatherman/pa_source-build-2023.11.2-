# Capital Expenditure Coverage Ratio Calculator
# ---------------------------------------------
# Overview:
# The Capital Expenditure Coverage Ratio indicates how many times a company can cover its capital expenditures
# from its operating cash flow. It provides insights into the firm's ability to fund its capital expenditures 
# without relying on external sources of finance.
#
# Formula:
# Capital Expenditure Coverage Ratio = Cash Flow from Operations / Capital Expenditures
#
# Desired Value:
# A higher ratio indicates a stronger ability of the company to finance its capital expenditures from 
# its operating cash flow. A ratio less than 1 indicates reliance on external financing or depletion 
# of cash reserves for capital expenditures.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Cash Flow from Operations (in million dollars format for simplicity)
cash_flow_from_operations_in_millions = 1583.00  
cash_flow_from_operations = convert_to_actual_value(cash_flow_from_operations_in_millions)

# Capital Expenditures (in million dollars format for simplicity)
capital_expenditures_in_millions = -900.00  
capital_expenditures = convert_to_actual_value(capital_expenditures_in_millions)

# Hard-coded values for industry average

# Industry Average Cash Flow from Operations (in million dollars format for simplicity)
industry_avg_cash_flow_from_operations_in_millions = 1450.00  # Example value
industry_avg_cash_flow_from_operations = convert_to_actual_value(industry_avg_cash_flow_from_operations_in_millions)

# Industry Average Capital Expenditures (in million dollars format for simplicity)
industry_avg_capital_expenditures_in_millions = -850.00  # Example value
industry_avg_capital_expenditures = convert_to_actual_value(industry_avg_capital_expenditures_in_millions)

# Calculate Capital Expenditure Coverage Ratio for the company and the industry
capex_coverage_ratio = cash_flow_from_operations / capital_expenditures
industry_avg_capex_coverage_ratio = industry_avg_cash_flow_from_operations / industry_avg_capital_expenditures

# Output the results
print(f"Company's Capital Expenditure Coverage Ratio: {capex_coverage_ratio:.2f}")
print(f"Industry Average Capital Expenditure Coverage Ratio: {industry_avg_capex_coverage_ratio:.2f}")

if capex_coverage_ratio > 3:
    print("The company has a strong ability to cover its capital expenditures multiple times with its operating cash flow.")
    if capex_coverage_ratio > industry_avg_capex_coverage_ratio:
        print("The company's Capital Expenditure Coverage Ratio is above the industry average, indicating a stronger financial position relative to peers.")
    else:
        print("The company's Capital Expenditure Coverage Ratio is below the industry average. It's essential to investigate the reasons and potential areas of improvement.")
elif capex_coverage_ratio > 1:
    print("The company can cover its capital expenditures with its operating cash flow.")
    if capex_coverage_ratio < industry_avg_capex_coverage_ratio:
        print("However, its ratio is below the industry average. Consider further investigation.")
else:
    print("The company may rely on external financing or use of cash reserves for its capital expenditures.")
