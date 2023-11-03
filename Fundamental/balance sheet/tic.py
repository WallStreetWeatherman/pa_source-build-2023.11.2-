# Total Invested Capital Approach Calculator
# ------------------------------------------
# Overview:
# This script calculates the Total Invested Capital (TIC) for a company.
# TIC provides a comprehensive measure of the company's value based on all sources of capital, both debt and equity.
#
# Formula:
# Total Invested Capital = Total Equity + Total Debt
#
# Desired Value:
# Generally, the 'right' value of Total Invested Capital will depend on the company's operations, industry standards,
# and its strategic goals. Higher TIC might mean more resources to deploy, but also might imply higher liabilities or equity dilution.
# It's essential to compare TIC with industry averages to determine if the company is over-leveraged or efficiently funded.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Total Equity (in million dollars format for simplicity)
total_equity_in_millions = 7500.00
total_equity = convert_to_actual_value(total_equity_in_millions)

# Total Debt (in million dollars format for simplicity)
total_debt_in_millions = 5000.00
total_debt = convert_to_actual_value(total_debt_in_millions)

# Hard-coded values for industry average

# Industry Average Total Equity (in million dollars format for simplicity)
industry_avg_total_equity_in_millions = 7000.00
industry_avg_total_equity = convert_to_actual_value(industry_avg_total_equity_in_millions)

# Industry Average Total Debt (in million dollars format for simplicity)
industry_avg_total_debt_in_millions = 4800.00
industry_avg_total_debt = convert_to_actual_value(industry_avg_total_debt_in_millions)

# Calculate Total Invested Capital for the company and industry average
tic = total_equity + total_debt
industry_avg_tic = industry_avg_total_equity + industry_avg_total_debt

# Convert back to millions for easier readability
tic_in_millions = tic / 1000000
industry_avg_tic_in_millions = industry_avg_tic / 1000000

# Output the results
print(f"Company's Total Invested Capital: ${tic_in_millions:.2f} million")
print(f"Industry Average Total Invested Capital: ${industry_avg_tic_in_millions:.2f} million")

if tic_in_millions > industry_avg_tic_in_millions:
    print("The company's TIC is higher than the industry average. This can be due to:")
    print("1. More equity funding through share issuance.")
    print("2. Higher borrowing compared to peers.")
    print("3. Significant reinvested earnings or retained profits.")
    print("\nIt's crucial to determine the cost of this capital and ensure it's deployed efficiently to generate desired returns.")
    
elif tic_in_millions == industry_avg_tic_in_millions:
    print("The company's TIC aligns with the industry average. This might indicate:")
    print("1. Similar funding structures as other players in the industry.")
    print("2. Balanced use of equity and debt financing.")
    print("\nIt would be helpful to assess the efficiency and returns on this capital compared to peers.")
    
else:
    print("The company's TIC is lower than the industry average. This might imply:")
    print("1. Less reliance on external funding, either debt or equity.")
    print("2. Efficient capital structuring with a focus on internal financing.")
    print("3. Possibly a smaller scale of operations compared to the industry peers.")
    print("\nWhile a lower TIC can suggest less financial risk, it's vital to assess the returns generated from the deployed capital and the company's growth strategy.")
