# Average Growth Rate Calculator for Financial Metrics
# ----------------------------------------------------
# Overview:
# This script calculates the average growth rates of key financial metrics over the past two years.
#
# Desired Value:
# Positive growth in Operating Income and Depreciation and Amortization, 
# minimized growth or even negative growth in CapEx, Working Capital, and Interest Expenses.

# Function to calculate growth rate
def calculate_growth_rate(initial_value, final_value, periods=1):
    try:
        return ((final_value / initial_value) ** (1 / periods) - 1) * 100
    except ZeroDivisionError:
        return 0

# Hard-coded past two years data (in millions e.g., 1.00 = $1 million)
# Year 1 Data
operating_income_y1 = 2334.00
depreciation_and_amortization_y1 = 634.00
capex_y1 = 354.00
working_capital_y1 = 195.00
interest_expense_y1 = 256.00

# Year 2 Data
operating_income_y2 = 1681.00
depreciation_and_amortization_y2 = 620.00
capex_y2 = 888.00
working_capital_y2 = -454.00
interest_expense_y2 = 175.00

# Calculate average growth rates
operating_income_growth = calculate_growth_rate(operating_income_y1, operating_income_y2, 1)
depreciation_growth = calculate_growth_rate(depreciation_and_amortization_y1, depreciation_and_amortization_y2, 1)
capex_growth = calculate_growth_rate(capex_y1, capex_y2, 1)
working_capital_growth = calculate_growth_rate(working_capital_y1, working_capital_y2, 1)
interest_expense_growth = calculate_growth_rate(interest_expense_y1, interest_expense_y2, 1)

# Output the results
print(f"Average Growth Rate for Operating Income: {operating_income_growth:.2f}%")
print(f"Average Growth Rate for Depreciation and Amortization: {depreciation_growth:.2f}%")
print(f"Average Growth Rate for Capital Expenditure (CapEx): {capex_growth:.2f}%")
print(f"Average Growth Rate for Change in Working Capital: {working_capital_growth:.2f}%")
print(f"Average Growth Rate for Interest Expense: {interest_expense_growth:.2f}%")
