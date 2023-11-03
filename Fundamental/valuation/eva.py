# Economic Value Added (EVA) Calculator
# -------------------------------------
# Overview:
# Economic Value Added (EVA) evaluates a company's true economic profit after considering 
# the total cost of capital. It's defined as the net operating profit after taxes (NOPAT) 
# minus the capital charge (the cost of capital multiplied by the capital invested).
#
# Desired Value:
# A positive EVA indicates that a company is generating returns above its cost of capital, 
# which is generally a sign of value creation. Conversely, a negative EVA suggests that the 
# company is not generating enough profit to cover its cost of capital, potentially destroying value.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# financial data should be sourced from the company's financial statements.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for a hypothetical company
nopat = convert_to_actual_value(15.00)  # Net Operating Profit After Taxes in actual value
capital_invested = convert_to_actual_value(100.00)  # Total capital invested in actual value
cost_of_capital = 0.08  # Company's cost of capital (8% as an example)

def eva_calculator(nopat, capital_invested, cost_of_capital):
    capital_charge = capital_invested * cost_of_capital
    eva = nopat - capital_charge
    return eva

economic_value_added = eva_calculator(nopat, capital_invested, cost_of_capital)

# Output the result
print("Economic Value Added (EVA) Calculation:\n")
print("Net Operating Profit After Taxes (NOPAT): ${:,.2f}".format(nopat / 1000000))
print("Total Capital Invested: ${:,.2f}".format(capital_invested / 1000000))
print("Company's Cost of Capital: {:.2%}".format(cost_of_capital))
print("\nEconomic Value Added (EVA): ${:,.2f}".format(economic_value_added / 1000000))

