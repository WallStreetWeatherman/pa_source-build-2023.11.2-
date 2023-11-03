# Capital Invested Calculator
# ---------------------------
# Overview:
# Capital Invested provides a measure of the total amount of money that shareholders and debt holders have invested in a company.
# It is often used in efficiency ratios to gauge how well a company is using its capital to generate profits.
#
# Formula:
# Capital Invested = Total Equity + Total Debt - Cash & Cash Equivalents
#
# Desired Value:
# The 'right' amount of Capital Invested is subjective and depends largely on the industry, the company's stage of development, 
# and its strategy. Generally, a company should aim to efficiently deploy its capital to generate profitable returns.
# A comparison with industry averages or competitors can offer valuable insights.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Total Equity (in million dollars format for simplicity)
total_equity_in_millions = 4082.00  # Total Equity in Tikr
total_equity = convert_to_actual_value(total_equity_in_millions)

# Total Debt (in million dollars format for simplicity)
total_debt_in_millions = 6294.00  # Total Debt in Tikr
total_debt = convert_to_actual_value(total_debt_in_millions)

# Cash & Cash Equivalents (in million dollars format for simplicity)
cash_equivalents_in_millions = 862.00  # Cash & Equivalents in Tikr
cash_equivalents = convert_to_actual_value(cash_equivalents_in_millions)

# Hard-coded values for industry average

# Industry Average Total Equity (in million dollars format for simplicity)
industry_avg_total_equity_in_millions = 4220.00
industry_avg_total_equity = convert_to_actual_value(industry_avg_total_equity_in_millions)

# Industry Average Total Debt (in million dollars format for simplicity)
industry_avg_total_debt_in_millions = 1270.00
industry_avg_total_debt = convert_to_actual_value(industry_avg_total_debt_in_millions)

# Industry Average Cash & Cash Equivalents (in million dollars format for simplicity)
industry_avg_cash_equivalents_in_millions = 756.00
industry_avg_cash_equivalents = convert_to_actual_value(industry_avg_cash_equivalents_in_millions)

# Calculate Capital Invested for the company and industry average
capital_invested = total_equity + total_debt - cash_equivalents
industry_avg_capital_invested = industry_avg_total_equity + industry_avg_total_debt - industry_avg_cash_equivalents

# Convert back to millions for easier readability
capital_invested_in_millions = capital_invested / 1000000
industry_avg_capital_invested_in_millions = industry_avg_capital_invested / 1000000

# Output the results
print(f"Company's Capital Invested: ${capital_invested_in_millions:.2f} million")
print(f"Industry Average Capital Invested: ${industry_avg_capital_invested_in_millions:.2f} million")

if capital_invested_in_millions > industry_avg_capital_invested_in_millions:
    print("The company has a higher Capital Invested than the industry average. This could be due to:")
    print("1. Expansion or growth strategies requiring higher investments.")
    print("2. Acquisitions or mergers that might have taken place recently.")
    print("3. Capital-intensive nature of the business operations.")
    print("4. Possible inefficiencies in capital deployment.")
    print("\nIt's essential to evaluate the returns generated from this capital and compare it with the industry average to gauge efficiency.")
    
elif capital_invested_in_millions == industry_avg_capital_invested_in_millions:
    print("The company's Capital Invested aligns with the industry average. This indicates:")
    print("1. The company is in line with industry norms in terms of capital deployment.")
    print("2. The risk profile in terms of debt and equity mix might be similar to other industry players.")
    print("3. The company's growth rate might be consistent with the industry.")
    print("\nIt would be beneficial to assess the efficiency and returns on this capital relative to peers.")
    
else:
    print("The company has a lower Capital Invested than the industry average. This might suggest:")
    print("1. The company operates more efficiently with less capital.")
    print("2. The business model might be less capital-intensive than peers.")
    print("3. The company could be in a different growth phase, requiring less external financing.")
    print("4. There might be significant cash reserves, reducing net invested capital.")
    print("\nWhile a lower capital invested might indicate efficiency, the returns generated from the capital and the company's growth strategy should be thoroughly evaluated.")
