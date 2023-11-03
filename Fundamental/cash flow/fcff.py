# Free Cash Flow to the Firm Calculator
# -------------------------------------
# Overview:
# The Free Cash Flow to the Firm (FCFF) indicates the amount of cash that's available to both equity 
# shareholders and debtholders. It reflects the efficiency of the firm's operations and investment decisions.
#
# Formula:
# FCFF = EBIT * (1 - tax rate) + Depreciation & Amortization - Change in Net Working Capital - Capital Expenditures (CapEx)
#
# Desired Value:
# A positive FCFF indicates the company is generating more cash than it needs to fund operations and capital expenditures, 
# suggesting it has surplus cash available for either debtholders or equity shareholders. A negative FCFF may signal 
# potential liquidity or profitability concerns.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value_in_millions * 1000000

# Hard-coded values for the company
company_ebit_in_millions = 23005.00
company_ebit = convert_to_actual_value(company_ebit_in_millions)

company_tax_rate = 0.21  
company_depreciation_amortization_in_millions = 642.00
company_depreciation_amortization = convert_to_actual_value(company_depreciation_amortization_in_millions)

company_change_nwc_in_millions = -208.00
company_change_nwc = convert_to_actual_value(company_change_nwc_in_millions)

company_capex_in_millions = 900.00
company_capex = convert_to_actual_value(company_capex_in_millions)

# Calculate the company's FCFF
company_fcff = (company_ebit * (1 - company_tax_rate)) + company_depreciation_amortization - company_change_nwc - company_capex

# Hard-coded values for industry average (for demonstration purposes)
industry_avg_ebit_in_millions = 22000.00
industry_avg_ebit = convert_to_actual_value(industry_avg_ebit_in_millions)

industry_avg_depreciation_amortization_in_millions = 600.00
industry_avg_depreciation_amortization = convert_to_actual_value(industry_avg_depreciation_amortization_in_millions)

industry_avg_change_nwc_in_millions = -200.00
industry_avg_change_nwc = convert_to_actual_value(industry_avg_change_nwc_in_millions)

industry_avg_capex_in_millions = 850.00
industry_avg_capex = convert_to_actual_value(industry_avg_capex_in_millions)

# Calculate the industry average FCFF
industry_avg_fcff = (industry_avg_ebit * (1 - company_tax_rate)) + industry_avg_depreciation_amortization - industry_avg_change_nwc - industry_avg_capex

# Output the results
print("Free Cash Flow to the Firm Calculation:\n")
print(f"Company's Free Cash Flow to the Firm (FCFF): ${company_fcff/1000000:.2f} million")
print(f"Industry Average Free Cash Flow to the Firm (FCFF): ${industry_avg_fcff/1000000:.2f} million\n")

# Interpretation
if company_fcff > industry_avg_fcff:
    print("The company's FCFF is higher than the industry average, suggesting a more robust financial position and operational efficiency compared to its peers. Potential reasons include:")
    print("- Higher operational profit margins, reflected by the EBIT.")
    print("- Effective tax management, possibly through tax incentives or efficient tax planning.")
    print("- Amortization and depreciation benefits derived from prior asset acquisitions.")
    print("- Efficient management of working capital, reflecting in the change in NWC.")
    print("- Strategic decision-making that resulted in optimal CapEx spending, either by leveraging technological advancements or cost-saving measures.")
    
elif company_fcff == industry_avg_fcff:
    print("The company's FCFF is in line with the industry average. This indicates:")
    print("- Operational and investment efficiencies comparable to industry norms.")
    print("- A balance in the management of working capital and capital expenditure, mirroring industry trends.")
    print("- Consistency in generating operational profits in line with its competitors.")
    
else:
    print("The company's FCFF is lower than the industry average. This might be due to several reasons:")
    print("- Potentially slimmer operational margins or challenges faced in generating consistent operational profits.")
    print("- Higher capital expenditures, which could be due to aggressive expansion, technological upgrades, or replacing outdated assets.")
    print("- Potential inefficiencies in managing working capital, perhaps due to slower inventory turnover or difficulties in managing receivables and payables.")
    print("- The company might be incurring higher taxes, either due to a lack of tax planning or being ineligible for specific tax benefits available to peers.")
    print("- Lower values of depreciation and amortization, suggesting that the company might have a relatively younger set of assets compared to peers.")
    
