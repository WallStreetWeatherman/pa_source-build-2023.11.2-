# Times Interest Earned Ratio (TIE) Calculator
# -------------------------------------------
# Overview:
# The Times Interest Earned Ratio (TIE) is a measure of a company's ability to cover its interest expenses with its operating income.
# It helps investors and analysts understand how comfortably a company can pay interest on its outstanding debt.
# The TIE is often referred to as the interest coverage ratio and used interchangeably.
#
# Formula:
# TIE = Operating Income / Interest Expense
#
# Desired Value:
# A higher TIE value indicates a better ability to cover interest expenses. A lower value may suggest potential difficulty in meeting interest obligations.
#

# Company's data:
operating_income_company = 1681.00 # operating income in tikr
interest_expense_company = 175.00 # interest expense in tikr

# Industry average data:
operating_income_industry = 479.00
interest_expense_industry = 37.00

# Company's TIE calculation
TIE_company = operating_income_company / interest_expense_company

# Industry average TIE calculation
TIE_industry = operating_income_industry / interest_expense_industry

# Display results
print(f"Company's Operating Income (in $1M): ${operating_income_company:.2f}M")
print(f"Company's Interest Expense (in $1M): ${interest_expense_company:.2f}M")
print(f"Company's Times Interest Earned Ratio (TIE): {TIE_company:.2f}\n")

print(f"Industry Average Operating Income (in $1M): ${operating_income_industry:.2f}M")
print(f"Industry Average Interest Expense (in $1M): ${interest_expense_industry:.2f}M")
print(f"Industry Average Times Interest Earned Ratio (TIE): {TIE_industry:.2f}\n")

# Provide insights and potential influencing factors
if TIE_company > TIE_industry:
    print("The company's TIE is above the industry average, signifying a robust capacity to meet interest obligations.")
    print("\nFactors potentially influencing a higher TIE include:")
    print("- Strong operating performance and profitability.")
    print("- Successful cost control measures leading to higher operating income.")
    print("- Prudent debt management with reasonable interest obligations.")
    print("- Benefit from favorable interest rates or terms on debt.")
    
elif TIE_company < TIE_industry:
    print("The company's TIE is below the industry average, suggesting potential challenges in covering interest expenses.")
    print("\nPossible factors contributing to a lower TIE are:")
    print("- Decreased operating income due to competitive pressures or decreased sales.")
    print("- Increased interest expenses from taking on high-interest debt or renegotiated loan terms.")
    print("- Existence of non-operating expenses reducing overall income.")
    print("- Adverse market or economic conditions impacting profitability.")
    
else:
    print("The company's TIE aligns with the industry average.")
    print("\nIt suggests the company is managing its debt and interest expenses in line with industry norms.")
    