# Net Operating Assets (NOA) Approach Calculator
# ----------------------------------------------
# Overview:
# This script calculates Capital Invested using the Net Operating Assets (NOA) approach.
# NOA provides a measure of the total operating assets used in the company's core operations
# minus the non-interest bearing current liabilities.
#
# Formula:
# Capital Invested = Total Assets - Non-Interest Bearing Current Liabilities
#
# Desired Value:
# The 'right' amount of Net Operating Assets depends largely on the industry, the company's 
# stage of development, and its strategy. Typically, a higher NOA implies more assets are tied 
# in operations. A comparison with industry averages or competitors can offer valuable insights.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Total Assets (in million dollars format for simplicity)
total_assets_in_millions = 15245.00  # Total Assets in Financial Statement
total_assets = convert_to_actual_value(total_assets_in_millions)

# Non-Interest Bearing Current Liabilities (in million dollars format for simplicity)
non_interest_liabilities_in_millions = 2458.00  # Non-Interest Bearing Current Liabilities in Financial Statement
non_interest_liabilities = convert_to_actual_value(non_interest_liabilities_in_millions)

# Hard-coded values for industry average

# Industry Average Total Assets (in million dollars format for simplicity)
industry_avg_total_assets_in_millions = 15000.00
industry_avg_total_assets = convert_to_actual_value(industry_avg_total_assets_in_millions)

# Industry Average Non-Interest Bearing Current Liabilities (in million dollars format for simplicity)
industry_avg_non_interest_liabilities_in_millions = 2300.00
industry_avg_non_interest_liabilities = convert_to_actual_value(industry_avg_non_interest_liabilities_in_millions)

# Calculate NOA for the company and industry average
noa = total_assets - non_interest_liabilities
industry_avg_noa = industry_avg_total_assets - industry_avg_non_interest_liabilities

# Convert back to millions for easier readability
noa_in_millions = noa / 1000000
industry_avg_noa_in_millions = industry_avg_noa / 1000000

# Output the results
print(f"Company's Net Operating Assets (NOA): ${noa_in_millions:.2f} million")
print(f"Industry Average Net Operating Assets (NOA): ${industry_avg_noa_in_millions:.2f} million")

if noa_in_millions > industry_avg_noa_in_millions:
    print("The company has a higher NOA than the industry average. This could imply more assets are committed to operations, possibly due to:")
    print("1. Expansion strategies or capital-intensive business operations.")
    print("2. Investments in long-term assets to support business growth.")
    print("3. Relatively lower non-interest bearing liabilities.")
    print("\nEvaluating the returns generated from these operating assets in comparison to the industry can offer deeper insights.")
    
elif noa_in_millions == industry_avg_noa_in_millions:
    print("The company's NOA aligns with the industry average. This indicates conformity with industry norms in terms of operational asset allocation.")
    print("A review of the efficiency and returns on these operating assets relative to peers would be beneficial.")
    
else:
    print("The company has a lower NOA than the industry average. This might suggest:")
    print("1. More efficient operations with fewer assets.")
    print("2. A less capital-intensive business model compared to peers.")
    print("3. Higher non-interest bearing liabilities offsetting total assets.")
    print("\nWhile a lower NOA might indicate efficiency, it's crucial to assess the returns generated from these assets and the company's growth strategy.")
