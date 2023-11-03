# Adjusted Present Value (APV) Model
# ----------------------------------
# Overview:
# The Adjusted Present Value (APV) approach values a business in two parts: the 
# value of the business without any debt (unlevered value using DCF) and the value 
# of its debt benefits, like tax shields due to interest payments.
#
# Desired Value:
# A high APV value indicates that, after accounting for the benefits of leverage, 
# the company has substantial intrinsic worth. A low or negative APV might 
# signify that the firm's value, even after considering debt benefits, is limited.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from financial projections and capital structure analysis.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def unlevered_dcf(free_cash_flows, discount_rate):
    """Calculate the unlevered value of the business using DCF."""
    total_value = 0
    for i, fcf in enumerate(free_cash_flows):
        total_value += fcf / (1 + discount_rate) ** (i + 1)
    return total_value

def tax_shield(debt, interest_rate, tax_rate, years):
    """Calculate the PV of tax shield given debt, interest rate, tax rate, and number of years."""
    annual_tax_shield = debt * interest_rate * tax_rate
    total_tax_shield = 0
    for i in range(years):
        total_tax_shield += annual_tax_shield / (1 + interest_rate) ** (i + 1)
    return total_tax_shield

# Hard-coded values for demonstration:
free_cash_flows = [convert_to_actual_value(10.00), 
                   convert_to_actual_value(11.00),
                   convert_to_actual_value(12.50)] # Projected Free Cash Flows for the next three years
discount_rate = 0.1  # 10% annual discount rate for FCF
debt = convert_to_actual_value(50.00)  # Initial debt
interest_rate = 0.05  # Annual interest rate on the debt
tax_rate = 0.3  # Corporate tax rate
years = 3  # Duration for which projections are available

unlevered_value = unlevered_dcf(free_cash_flows, discount_rate)
tax_shield_value = tax_shield(debt, interest_rate, tax_rate, years)

apv = unlevered_value + tax_shield_value

# Output the result
print("Adjusted Present Value (APV) Model:\n")
print("Valuation of the Company: ${:,.2f} million".format(apv / 1000000))

