# Enterprise Value-to-Sales (EV/S) Calculation
# --------------------------------------------
# Overview:
# Enterprise Value-to-Sales (EV/S) is a valuation measure that compares the 
# enterprise value of a company to its sales. It's similar to the Price-to-Sales (P/S) 
# ratio, but EV/S considers debt and other liabilities, offering a more comprehensive 
# view of a company's valuation.
#
# Desired Value:
# Like other valuation ratios, a "good" EV/S value depends on the industry and 
# the company's growth prospects. Generally, a lower EV/S ratio might indicate 
# that a company is undervalued, but this should be evaluated in context with 
# other factors.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from financial statements and market data.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def ev_to_sales(enterprise_value, total_sales):
    """
    Calculate EV/S ratio.
    
    Parameters:
    enterprise_value - Total value of a business, including market capitalization, 
                       debt, and other liabilities minus cash and cash equivalents
    total_sales - Company's total sales or revenue
    """
    return enterprise_value / total_sales

# Hard-coded values for demonstration:
market_cap = convert_to_actual_value(200.00)  # Company's market capitalization
debt = convert_to_actual_value(50.00)  # Company's total debt
other_liabilities = convert_to_actual_value(10.00)  # Other liabilities
cash_equivalents = convert_to_actual_value(30.00)  # Cash and cash equivalents

total_sales = convert_to_actual_value(100.00)  # Company's total sales

# Calculate Enterprise Value
enterprise_value = market_cap + debt + other_liabilities - cash_equivalents

ev_s_ratio = ev_to_sales(enterprise_value, total_sales)

# Output the result
print("Enterprise Value-to-Sales (EV/S) Calculation:\n")
print("EV/S Ratio for the Company: {:.2f}".format(ev_s_ratio))

