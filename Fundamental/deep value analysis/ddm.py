# Dividend Discount Model (DDM)
#
# Overview:
# The Dividend Discount Model (DDM) calculates the intrinsic value of a stock 
# based on the present value of expected future dividends. 
# It's particularly useful for companies that distribute regular dividends.
#
# Desired Value:
# A higher calculated intrinsic value compared to the current market price 
# would suggest that the stock may be undervalued. Conversely, a lower intrinsic 
# value suggests potential overvaluation.

def ddm(dividend, growth_rate, discount_rate):
    """
    Calculate the intrinsic value using the Dividend Discount Model.
    
    Parameters:
    - dividend: Next year's expected dividend. (e.g., for $1,000,000 use 1.00)
    - growth_rate: Expected dividend growth rate (as a decimal, e.g., 5% as 0.05)
    - discount_rate: Required rate of return or discount rate (as a decimal, e.g., 10% as 0.10)
    
    Returns:
    - Intrinsic value of the stock.
    """
    return dividend / (discount_rate - growth_rate)

# Hardcoded values for demonstration
dividend = 1.50  # Expected dividend for next year ($1,500,000)
growth_rate = 0.04  # Expected growth rate of 4%
discount_rate = 0.10  # Required rate of return of 10%

intrinsic_value = ddm(dividend, growth_rate, discount_rate)
print(f"The intrinsic value based on DDM is: ${intrinsic_value:.2f}")
