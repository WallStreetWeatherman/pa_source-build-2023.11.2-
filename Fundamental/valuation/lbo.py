# LBO (Leveraged Buyout) Valuation
# ------------------------------------------------
# Overview:
# LBO valuation models what a private equity firm might pay for a company based 
# on its required internal rate of return (IRR) and the potential financing structure.
# This script provides a basic LBO model with hard-coded values.
#
# Desired Value:
# The PE firm would desire the company's valuation (purchase price) to be as low as 
# possible to achieve its required IRR, given the future cash flow projections.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from market data and detailed company analysis.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def lbo_valuation(initial_value, debt_percentage, pe_required_irr, projected_cashflows, exit_multiple):
    """Simple LBO valuation model."""
    
    # Determine equity and debt amounts
    debt = initial_value * debt_percentage
    equity = initial_value - debt
    
    # Estimate future exit value of the company
    final_year_cashflow = projected_cashflows[-1]
    exit_value = final_year_cashflow * exit_multiple
    
    # Simulate the cashflows and debt paydown
    for cf in projected_cashflows:
        debt_paydown = min(debt, cf * 0.5)  # Assume 50% of cashflow is used to pay down debt
        debt -= debt_paydown
    
    # Calculate the final equity value after debt has been repaid
    final_equity_value = exit_value - debt
    
    # Compute IRR
    cashflows = [-equity] + [0] * (len(projected_cashflows) - 1) + [final_equity_value]
    irr = np.irr(cashflows)
    
    return irr

import numpy as np

# Hard-coded values for demonstration
initial_value = convert_to_actual_value(10.00)  # Initial purchase price, e.g., $10 million
debt_percentage = 0.6  # e.g., 60% of the purchase is financed by debt
pe_required_irr = 0.25  # e.g., 25% IRR requirement by the PE firm
projected_cashflows = [convert_to_actual_value(x) for x in [1.5, 1.6, 1.7, 1.9, 2.2]]  # Next 5 years' projected cashflows
exit_multiple = 5  # E.g., PE firm expects to sell the company at 5x the final year's cashflow

calculated_irr = lbo_valuation(initial_value, debt_percentage, pe_required_irr, projected_cashflows, exit_multiple)

# Output the result
print("LBO Valuation:\n")
print("Calculated IRR based on given assumptions: {:.2f}%".format(calculated_irr * 100))

if calculated_irr >= pe_required_irr:
    print("The deal meets the PE firm's required IRR.")
else:
    print("The deal does NOT meet the PE firm's required IRR.")

