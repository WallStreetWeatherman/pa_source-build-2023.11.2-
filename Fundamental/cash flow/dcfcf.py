# Dividend Coverage Ratio (from Cash Flows) Calculator
# ----------------------------------------------------
# Overview:
# The Dividend Coverage Ratio (from Cash Flows) measures the extent to which a company's cash flow from operations 
# covers its dividend payments. It provides insights into the sustainability of the company's dividends.
#
# Formula:
# Dividend Coverage Ratio (from Cash Flows) = Cash Flow from Operations / Total Dividends Paid
#
# Desired Value:
# A ratio greater than 1 indicates that the company generates sufficient cash flow to cover its dividend payments.
# A value less than 1 may suggest potential dividend sustainability issues in the future.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Cash Flow from Operations (in million dollars format for simplicity)
company_cash_flow_from_operations_in_millions = 1615.00 # Cash from Operations in Tikr
company_cash_flow_from_operations = convert_to_actual_value(company_cash_flow_from_operations_in_millions)

# Company Total Dividends Paid (in million dollars format for simplicity)
company_total_dividends_paid_in_millions = 173.00  # Common Dividends Paid in Tikr
company_total_dividends_paid = convert_to_actual_value(company_total_dividends_paid_in_millions)

# Hard-coded values for industry average

# Industry Average Cash Flow from Operations (in million dollars format for demonstration)
industry_avg_cash_flow_from_operations_in_millions = 803.00  
industry_avg_cash_flow_from_operations = convert_to_actual_value(industry_avg_cash_flow_from_operations_in_millions)

# Industry Average Total Dividends Paid (in million dollars format for demonstration)
industry_avg_total_dividends_paid_in_millions = 16.00  
industry_avg_total_dividends_paid = convert_to_actual_value(industry_avg_total_dividends_paid_in_millions)

# Calculate Dividend Coverage Ratio (from Cash Flows) for the company and industry
company_dividend_coverage_ratio = company_cash_flow_from_operations / company_total_dividends_paid
industry_dividend_coverage_ratio = industry_avg_cash_flow_from_operations / industry_avg_total_dividends_paid

# Output the results
print(f"Company's Dividend Coverage Ratio (from Cash Flows): {company_dividend_coverage_ratio:.2f}")
print(f"Industry Average Dividend Coverage Ratio (from Cash Flows): {industry_dividend_coverage_ratio:.2f}\n")

if company_dividend_coverage_ratio > industry_dividend_coverage_ratio:
    print("The company exceeds the industry average in Dividend Coverage Ratio, suggesting a more comfortable position to cover its dividends relative to its peers. Factors possibly influencing this could include:")
    print("- Strong operational cash flow generation.")
    print("- A conservative dividend policy ensuring dividends are easily covered by cash flows.")
    print("- Effective working capital management leading to higher operational cash inflows.")
    print("- Potential reinvestment strategies or deferred capital expenditures that boost current operational cash flows.")
    
elif company_dividend_coverage_ratio == industry_dividend_coverage_ratio:
    print("The company's Dividend Coverage Ratio aligns with the industry average. This could be influenced by:")
    print("- An industry-standard approach to dividend payments.")
    print("- Consistent operational cash generation patterns relative to industry norms.")
    print("- Typical capital expenditures and operational costs for the industry impacting cash generation.")
    
else:
    print("The company is below the industry average in Dividend Coverage Ratio, which might raise concerns about its ability to maintain dividends. Possible influencing factors include:")
    print("- Larger capital expenditures eating into operational cash flows.")
    print("- Potential operational inefficiencies leading to lower cash generation.")
    print("- Aggressive dividend policies which might not be sustainable with the current cash generation.")
    print("- Challenges in managing working capital, impacting operational cash flows.")
    