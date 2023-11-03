# Excess Return Model
# -------------------
# Overview:
# The Excess Return Model values a company based on its ability to generate returns 
# in excess of its cost of capital. It utilizes the company's Return on Invested 
# Capital (ROIC) and the Weighted Average Cost of Capital (WACC) to determine these 
# excess returns.
#
# Desired Value:
# A high value suggests that the company is anticipated to produce significant excess 
# returns in the future. Conversely, a low or negative value might indicate that the 
# firm isn't expected to generate returns above its cost of capital.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from financial projections and capital structure analysis.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def excess_return_valuation(invested_capital, roic, wacc, discount_rate, years):
    """
    Calculate the present value of excess returns.
    
    Parameters:
    invested_capital - Initial amount of invested capital
    roic - List of projected Return on Invested Capital for the given years
    wacc - List of projected Weighted Average Cost of Capital for the given years
    discount_rate - Annual discount rate
    years - Number of years for which projections are available
    """
    total_value = 0
    
    for i in range(years):
        excess_return = (roic[i] - wacc[i]) * invested_capital
        discounted_excess_return = excess_return / (1 + discount_rate)**(i+1)
        total_value += discounted_excess_return
        invested_capital += excess_return
        
    return total_value

# Hard-coded values for demonstration:
invested_capital = convert_to_actual_value(100.00) # Starting invested capital
roic = [0.12, 0.13, 0.14]  # Projected ROIC for the next three years
wacc = [0.08, 0.08, 0.08]  # Projected WACC for the next three years
discount_rate = 0.10  # 10% annual discount rate
years = 3

valuation = excess_return_valuation(invested_capital, roic, wacc, discount_rate, years)

# Output the result
print("Excess Return Model:\n")
print("Valuation of the Company: ${:,.2f} million".format(valuation / 1000000))

