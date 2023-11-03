# Abnormal Earnings Valuation Model
# ---------------------------------
# Overview:
# The Abnormal Earnings Valuation Model values a company based on its future earnings, 
# adjusting these earnings by subtracting a charge for equity capital. It essentially 
# captures the value created above and beyond the required return on equity.
#
# Desired Value:
# A high value implies that the company is expected to generate substantial abnormal 
# earnings in the future. Conversely, a low or negative value may indicate that the 
# company isn't expected to produce returns above the cost of equity.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from financial projections and equity analysis.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def abnormal_earnings_valuation(future_earnings, equity_charge, discount_rate, years):
    """
    Calculate the present value of abnormal earnings.
    
    Parameters:
    future_earnings - List of projected earnings for the given years
    equity_charge - List of charges for equity capital for the given years
    discount_rate - Annual discount rate
    years - Number of years for which projections are available
    """
    total_value = 0
    
    for i in range(years):
        abnormal_earning = future_earnings[i] - equity_charge[i]
        discounted_abnormal_earning = abnormal_earning / (1 + discount_rate)**(i+1)
        total_value += discounted_abnormal_earning
        
    return total_value

# Hard-coded values for demonstration:
future_earnings = [convert_to_actual_value(10.00), convert_to_actual_value(12.00), convert_to_actual_value(14.00)]
equity_charge = [convert_to_actual_value(5.00), convert_to_actual_value(5.50), convert_to_actual_value(6.00)]
discount_rate = 0.10  # 10% annual discount rate
years = 3

valuation = abnormal_earnings_valuation(future_earnings, equity_charge, discount_rate, years)

# Output the result
print("Abnormal Earnings Valuation Model:\n")
print("Valuation of the Company: ${:,.2f} million".format(valuation / 1000000))

