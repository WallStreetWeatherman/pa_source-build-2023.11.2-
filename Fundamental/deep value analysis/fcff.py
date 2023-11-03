# Free Cash Flow to Firm (FCFF) Calculation
# -----------------------------------------
# Overview:
# The FCFF represents the cash flow available to both equity and debt holders.
# Comparing FCFF to enterprise value can give insights into the company's cash flow generation relative to its value.
#
# Desired Value:
# A higher FCFF relative to the enterprise value might suggest that the company is generating strong cash flows 
# compared to its value, which can be a sign of undervaluation. On the other hand, a lower FCFF might indicate overvaluation.

# Hardcoded values (in the format where 1 million is represented as 1.00, etc.)
net_income = 10.00           # Net Income (e.g., $10 million)
non_cash_charges = 1.50      # Depreciation and Amortization (e.g., $1.5 million)
working_capital_change = -1.00 # Change in working capital (e.g., -$1 million)
capital_expenditures = -3.00  # Capital Expenditures (e.g., -$3 million)
enterprise_value = 50.00     # Enterprise Value (e.g., $50 million)

def calculate_fcff(net_income, non_cash_charges, working_capital_change, capital_expenditures):
    """Calculate FCFF based on the provided financial metrics."""
    return net_income + non_cash_charges + working_capital_change - capital_expenditures

fcff = calculate_fcff(net_income, non_cash_charges, working_capital_change, capital_expenditures)
fcff_to_ev_ratio = fcff / enterprise_value

print(f"Free Cash Flow to Firm (FCFF): ${fcff:.2f} million")
print(f"FCFF to Enterprise Value Ratio: {fcff_to_ev_ratio:.2%}")

# Interpretation
if fcff_to_ev_ratio > 0.10:  # Example threshold; this might vary based on industry and market conditions.
    print("The company appears to be generating strong cash flows relative to its value.")
else:
    print("The company might be overvalued based on its current cash flows.")
