# Residual Income Model (RIM) for Valuation
# -----------------------------------------
# Overview:
# The Residual Income Model (RIM) is a method for valuing a company based on its future 
# residual income. Residual income is calculated by deducting the equity charge 
# (equity capital multiplied by cost of equity) from the company's net income.
#
# Desired Value:
# A higher residual income indicates that the company is generating more income 
# than the expected return on its equity. A higher value suggests a more valuable company.
# However, it's essential to compare RIM values across peers and consider other 
# valuation metrics for a holistic analysis.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from financial statements and market data.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def residual_income(net_income, equity_capital, cost_of_equity):
    """
    Calculate residual income.
    
    Parameters:
    net_income - Company's net income for the year
    equity_capital - Total equity capital of the company
    cost_of_equity - Company's cost of equity (annualized)
    """
    equity_charge = equity_capital * cost_of_equity
    return net_income - equity_charge

# Hard-coded values for demonstration:
net_income = convert_to_actual_value(15.00)  # Net income of the company
equity_capital = convert_to_actual_value(100.00)  # Total equity capital of the company
cost_of_equity = 0.08  # Cost of equity (annualized, e.g., 8%)

rim_value = residual_income(net_income, equity_capital, cost_of_equity)

# Output the result
print("Residual Income Model (RIM) Valuation:\n")
print("Residual Income for the Company: ${:,.2f} million".format(rim_value / 1000000))

