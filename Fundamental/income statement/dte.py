# Debt to EBITDA Calculation
# --------------------------
# Overview:
# The Debt to EBITDA ratio is a leverage metric that gauges a company's ability to pay off its debt.
# It is calculated by dividing the company's total debt by its Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA).
#
# Desired Value:
# A lower Debt to EBITDA ratio suggests that the company has a better ability to pay off its debt.
# Typically, a ratio less than 3 is considered healthy for most industries, but this can vary by sector.

# Hardcoded values for the company (in the format where 1 million is represented as 1.00, etc.)
company_total_debt = 10.00    # Company's Total Debt (e.g., $10 million)
company_ebitda = 4.00         # Company's EBITDA (e.g., $4 million)

# Hardcoded values for the industry average
industry_total_debt = 15.00   # Industry Average Total Debt (e.g., $15 million)
industry_ebitda = 6.00        # Industry Average EBITDA (e.g., $6 million)

# Calculate Debt to EBITDA ratio
def calculate_debt_to_ebitda(total_debt, ebitda):
    """Calculate the Debt to EBITDA ratio."""
    if ebitda == 0:
        raise ValueError("EBITDA should not be zero to calculate the Debt to EBITDA ratio.")
    return total_debt / ebitda

# Calculate Debt to EBITDA for the company and the industry
debt_to_ebitda_company = calculate_debt_to_ebitda(company_total_debt, company_ebitda)
debt_to_ebitda_industry = calculate_debt_to_ebitda(industry_total_debt, industry_ebitda)

print("Factors Influencing Debt to EBITDA Ratio:")
print("- **Company's Growth Phase:** Younger, rapidly growing companies might have higher leverage as they borrow to invest, potentially leading to a higher ratio.")
print("- **Industry Capital Intensity:** Capital-intensive industries like utilities or manufacturing might typically operate with higher leverage, thus a higher Debt to EBITDA ratio.")
print("- **Interest Rates:** Low-interest rates might incentivize borrowing, affecting the total debt component.")
print("- **Company's Capital Structure:** Firms with a preference for debt financing over equity might have higher ratios.")
print("- **Operational Cash Flows:** Companies with strong, stable operational cash flows might be more comfortable taking on debt.")
print("- **Recent Acquisitions:** Debt-funded acquisitions can lead to a temporary spike in the ratio.")
print("- **EBITDA Stability:** Volatile EBITDA can result in fluctuating ratios. Firms with stable earnings might have a more predictable Debt to EBITDA trend.")
print("- **Economic Conditions:** A recession or downturn might squeeze EBITDA, raising the ratio even if debt levels remain constant.")

print("\nDebt to EBITDA Analysis:")
print(f"Company's Debt to EBITDA Ratio: {debt_to_ebitda_company:.2f}")
print(f"Industry Average Debt to EBITDA Ratio: {debt_to_ebitda_industry:.2f}\n")

# Interpretation
if debt_to_ebitda_company < 3:
    print("The company's Debt to EBITDA ratio is below 3, which is typically considered healthy for most industries.")
elif debt_to_ebitda_company >= 3:
    print("The company's Debt to EBITDA ratio is 3 or higher, indicating a need for careful analysis based on industry norms.")

if debt_to_ebitda_company < debt_to_ebitda_industry:
    print("The company has a Debt to EBITDA ratio below the industry average, suggesting a healthier ability to pay off its debt.")
else:
    print("The company's Debt to EBITDA ratio is above the industry average, indicating potential leverage concerns.")
    