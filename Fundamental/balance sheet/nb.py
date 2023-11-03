# Net Borrowing Calculator
# ------------------------
# Overview:
# The Net Borrowing metric indicates the net amount of new debt issued by a company. 
# It is calculated as the Debt Issued minus the Debt Repaid.
#
# Formula:
# Net Borrowing = Debt Issued - Debt Repaid
#
# Desired Value:
# A high Net Borrowing value implies the company is taking on a lot of new debt, which 
# could be good for growth but adds financial risk. A low or negative value suggests the 
# company is paying off more debt than it's borrowing, which could mean it's in a deleveraging phase.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# input data should be sourced from financial statements or other reliable sources.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Debt Issued
company_debt_issued_in_millions = 1959.00
company_debt_issued = convert_to_actual_value(company_debt_issued_in_millions)

# Debt Repaid
company_debt_repaid_in_millions = 2005.00
company_debt_repaid = convert_to_actual_value(company_debt_repaid_in_millions)

# Calculate Net Borrowing for the company
company_net_borrowing = company_debt_issued - company_debt_repaid

# Hard-coded values for the industry average

# Debt Issued
industry_average_debt_issued_in_millions = 1900.00  # Placeholder value
industry_average_debt_issued = convert_to_actual_value(industry_average_debt_issued_in_millions)

# Debt Repaid
industry_average_debt_repaid_in_millions = 1850.00  # Placeholder value
industry_average_debt_repaid = convert_to_actual_value(industry_average_debt_repaid_in_millions)

# Calculate Net Borrowing for the industry average
industry_average_net_borrowing = industry_average_debt_issued - industry_average_debt_repaid

# Output the results
print(f"Company Net Borrowing: ${company_net_borrowing/1000000:.2f} million")
print(f"Industry Average Net Borrowing: ${industry_average_net_borrowing/1000000:.2f} million")

# Compare company's Net Borrowing with industry average and Discuss Influencing Factors
if company_net_borrowing > industry_average_net_borrowing:
    print("\nThe company's Net Borrowing is higher than the industry average. Factors to consider might include:")
    print("- Capital-intensive projects or expansion strategies.")
    print("- Refinancing existing debt at favorable terms.")
    print("- Timing mismatch between cash inflows and debt repayment schedules.")
elif company_net_borrowing < industry_average_net_borrowing:
    print("\nThe company's Net Borrowing is lower than the industry average. This could be due to:")
    print("- An active deleveraging strategy.")
    print("- Higher cash generation from operations, reducing the need for new debt.")
    print("- Conservative financial management, avoiding excessive leverage.")
else:
    print("\nThe company's Net Borrowing aligns with the industry average. Potential influencing factors could be:")
    print("- Industry-standard capital allocation and debt management strategies.")
    print("- A balanced approach between leveraging and deleveraging.")