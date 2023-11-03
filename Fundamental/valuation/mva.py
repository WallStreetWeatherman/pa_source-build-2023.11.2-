# Market Value Added (MVA) Calculation
# ------------------------------------
# Overview:
# Market Value Added (MVA) is a measure that represents the difference between 
# the market capitalization of a company and the capital contributed by investors.
# It essentially indicates how much value the company's management has created 
# for its shareholders.
#
# Desired Value:
# A positive MVA indicates that the company's management has created value for 
# its shareholders, while a negative MVA suggests that the value has been destroyed.
# Generally, a higher MVA is desirable as it indicates better performance 
# and value creation.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from financial statements and market data.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def market_value_added(market_cap, capital_invested):
    """
    Calculate MVA.
    
    Parameters:
    market_cap - Market capitalization of the company
    capital_invested - Capital contributed by investors
    """
    return market_cap - capital_invested

# Hard-coded values for demonstration:
market_cap = convert_to_actual_value(150.00)  # Market capitalization of the company
capital_invested = convert_to_actual_value(100.00)  # Capital contributed by investors

mva_value = market_value_added(market_cap, capital_invested)

# Output the result
print("Market Value Added (MVA) Calculation:\n")
print("MVA for the Company: ${:,.2f} million".format(mva_value / 1000000))

