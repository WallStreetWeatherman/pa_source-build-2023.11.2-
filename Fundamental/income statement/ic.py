# Interest Coverage Ratio Calculator
# ----------------------------------
# Overview:
# The Interest Coverage Ratio (ICR) measures how many times a company can cover its interest 
# expenses with its operating income. A higher ICR suggests that the company is better 
# positioned to meet its interest obligations.
#
# Formula:
# Interest Coverage Ratio = Operating Income / Interest Expense
# 
# Desired Value:
# A higher ICR is typically seen as favorable, as it suggests the company is financially 
# healthy and less vulnerable to fluctuations in interest rates or downturns in its business cycle.
# A low ICR may raise concerns about the company's ability to meet its interest obligations.

# Hard-coded values for the company:
operating_income_company = 1681.00  # Operating Income in Tikr
interest_expense_company = 175.00  # Interest Expense in Tikr

# Industry average values:
operating_income_industry = 479.00  
interest_expense_industry = 37.00  

# Calculate Interest Coverage Ratio for the company
interest_coverage_ratio_company = operating_income_company / interest_expense_company

# Calculate Interest Coverage Ratio for the industry average
interest_coverage_ratio_industry = operating_income_industry / interest_expense_industry

# Output the results
print(f"Company's Interest Coverage Ratio: {interest_coverage_ratio_company:.2f}")
print(f"Industry Average Interest Coverage Ratio: {interest_coverage_ratio_industry:.2f}")

# Interpretation
if interest_coverage_ratio_company > interest_coverage_ratio_industry:
    print("The company's Interest Coverage Ratio is above the industry average, suggesting stronger financial health and a better position to manage its debt obligations.")
    print("\nFactors possibly contributing to a higher ICR include:")
    print("- Consistent growth in operating income.")
    print("- Reduced borrowing or refinancing of debt at lower interest rates.")
    print("- Effective financial management strategies to optimize expenses.")
elif interest_coverage_ratio_company < interest_coverage_ratio_industry:
    print("The company's Interest Coverage Ratio is below the industry average, indicating potential challenges in meeting its interest expenses, especially in times of financial stress.")
    print("\nPotential reasons for a lower ICR might include:")
    print("- Increased borrowing which leads to higher interest expenses.")
    print("- Declining operating income due to reduced sales or increased costs.")
    print("- Exposures to variable interest rates that have recently risen.")
else:
    print("The company's Interest Coverage Ratio aligns with the industry average, indicating a comparable financial position to its peers.")
    