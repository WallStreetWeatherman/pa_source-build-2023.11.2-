# Forecasted FCFF and FCFE Calculator for Next Five Years
# -------------------------------------------------------
# Overview:
# This script calculates the forecasted Free Cash Flow to the Firm (FCFF) and 
# Free Cash Flow to Equity (FCFE) for the next five years based on the initial financial metrics.
#
# Desired Value:
# Higher values of FCFF and FCFE are generally more favorable, indicating stronger
# future cash-generating capability.
#
# Note: The script uses hard-coded values for demonstration. For real-world applications, 
# replace these with actual financial data.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000  # Convert to actual dollar amounts

# Hard-coded values (in millions, e.g., 1.00 = $1 million)
operating_income = 1204.00  # Operating income
tax_rate = 0.21  # Federal income statutory rate 21%
depreciation_and_amortization = 640.00  # Depreciation and Amortization
capex = 900.00  # Capital expenditure
change_in_working_capital = 208.00  # Change in working capital
interest_expense = 159.00  # Interest expense
net_borrowing = -290.00  # Net borrowing (new debt - debt repaid); negative indicates net outflow

# Growth rates for the next five years
operating_income_growth = -0.27  
depreciation_growth = -0.02  
capex_growth = 1.50  
working_capital_growth = -1.32  
interest_expense_growth = -0.31  

for year in range(1, 6):  # Loop through the next five years
    print(f"Year {year}:")

    # Apply the growth rates
    operating_income *= (1 + operating_income_growth)
    depreciation_and_amortization *= (1 + depreciation_growth)
    capex *= (1 + capex_growth)
    change_in_working_capital *= (1 + working_capital_growth)
    interest_expense *= (1 + interest_expense_growth)

    # Convert to actual values
    operating_income_actual = convert_to_actual_value(operating_income)
    depreciation_and_amortization_actual = convert_to_actual_value(depreciation_and_amortization)
    capex_actual = convert_to_actual_value(capex)
    change_in_working_capital_actual = convert_to_actual_value(change_in_working_capital)
    interest_expense_actual = convert_to_actual_value(interest_expense)
    net_borrowing_actual = convert_to_actual_value(net_borrowing)

    # Calculate FCFF
    fcff = (operating_income_actual * (1 - tax_rate)) + depreciation_and_amortization_actual - capex_actual - change_in_working_capital_actual
    fcff_in_millions = fcff / 1000000  # Convert back to million-dollar format

    # Calculate FCFE
    fcfe = fcff - (interest_expense_actual * (1 - tax_rate)) + net_borrowing_actual
    fcfe_in_millions = fcfe / 1000000  # Convert back to million-dollar format

    # Output the results
    print(f"  Forecasted Free Cash Flow to the Firm (FCFF): ${fcff_in_millions:.2f} million")
    print(f"  Forecasted Free Cash Flow to Equity (FCFE): ${fcfe_in_millions:.2f} million")
    print("="*40)
