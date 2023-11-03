# Free Cash Flow to Equity (FCFE) Calculation
# ------------------------------------------
# Overview:
# FCFE represents the cash flow available to equity holders after all business expenses, 
# taxes, interest, and principal repayments are met.
#
# Desired Value:
# A higher FCFE indicates that more cash is available to equity holders, which can be used 
# for dividends, stock buybacks, or reinvested into the business. A higher FCFE can be an 
# indicator of strong financial health.

# Hardcoded values (in the format where 1 million is represented as 1.00, etc.)
net_income = 15.00           # Net Income (e.g., $15 million)
capital_expenditures = -4.00 # Capital Expenditures (e.g., -$4 million)
debt_repayment = -2.50       # Principal Repayments (e.g., -$2.5 million)
debt_issued = 3.00           # New Debt Issued (e.g., $3 million)
working_capital_change = -1.50 # Change in working capital (e.g., -$1.5 million)

def calculate_fcfe(net_income, capital_expenditures, debt_repayment, debt_issued, working_capital_change):
    """Calculate FCFE based on the provided financial metrics."""
    return net_income + capital_expenditures + debt_repayment + debt_issued + working_capital_change

fcfe = calculate_fcfe(net_income, capital_expenditures, debt_repayment, debt_issued, working_capital_change)

print(f"Free Cash Flow to Equity (FCFE): ${fcfe:.2f} million")

# Interpretation
if fcfe > 0:
    print("Positive FCFE indicates the company has cash left after meeting all obligations, which is favorable for equity holders.")
else:
    print("Negative FCFE suggests that the company might be struggling to generate enough cash for its equity holders.")
