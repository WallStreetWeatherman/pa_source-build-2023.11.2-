# Book Value-to-Market Value Calculation
# --------------------------------------
# Overview:
# The Book Value-to-Market Value ratio compares a company's book value to its market value. 
# This ratio can be used to identify potential mismatches between the accounting value 
# of a company (book value) and how the market perceives its value.
#
# Desired Value:
# A ratio below 1 might suggest that the market undervalues the company compared to its 
# book value. However, it's crucial to understand the broader context, like industry 
# dynamics, growth prospects, and other financial metrics before drawing conclusions.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from financial statements and market data.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def bv_to_mv_ratio(book_value, market_value):
    """
    Calculate Book Value-to-Market Value ratio.
    
    Parameters:
    book_value - Company's book value (total assets minus total liabilities)
    market_value - Current market value or market capitalization of the company
    """
    return book_value / market_value

# Hard-coded values for the company
book_value = convert_to_actual_value(4210.00)  # Book value of the company
market_value = convert_to_actual_value(3141.00)  # Market value of the company

# Hard-coded values for industry average
industry_avg_book_value = convert_to_actual_value(4000.00)  # Industry average book value
industry_avg_market_value = convert_to_actual_value(3600.00)  # Industry average market value

# Calculate BV/MV Ratio for the company and industry
ratio_company = bv_to_mv_ratio(book_value, market_value)
ratio_industry = bv_to_mv_ratio(industry_avg_book_value, industry_avg_market_value)

# Output results and interpretation
print("Calculated BV/MV Ratio for the Company: {:.2f}".format(ratio_company))
print("Industry Average BV/MV Ratio: {:.2f}".format(ratio_industry))

if ratio_company < ratio_industry:
    print("The company's BV/MV Ratio is below the industry average, suggesting it may be undervalued.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Lower Market Perception: The market may be undervaluing the company's assets or future potential.")
    print("2. Underexplored Assets: The company might possess assets that have not been fully monetized.")
elif ratio_company > ratio_industry:
    print("The company's BV/MV Ratio is above the industry average, suggesting it may be overvalued.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Market Exuberance: High investor demand could be driving up the market valuation.")
    print("2. Deteriorating Assets: The company might be holding assets that are declining in value.")
else:
    print("The company's BV/MV Ratio is in line with the industry average.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Market Alignment: The company is priced similarly to its industry peers.")
    print("2. Stable Assets: The assets are generally perceived as valuable as the industry average.")
