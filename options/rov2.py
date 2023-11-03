import math
from scipy.stats import norm

# Real Options Valuation using Black-Scholes Model
# ------------------------------------------------
# Overview:
# The Real Options Valuation (ROV) approach treats certain business decisions as 
# "options" and uses financial option pricing models to value them. This script 
# demonstrates a basic ROV using the Black-Scholes model.
#
# Desired Value:
# Higher values indicate that the "option" to pursue a business decision has a 
# greater intrinsic value, given the underlying assumptions. However, the interpretation 
# will depend on the specific business decision and context.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from market data and detailed analysis.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes option price for a European call.
    
    Parameters:
    S - Current stock price
    K - Option strike price
    T - Time to maturity (in years)
    r - Risk-free rate (annualized)
    sigma - Stock price volatility (annualized)
    """
    
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

# Hard-coded values for demonstration:
S = convert_to_actual_value(5.00)  # Current project value (or stock price in traditional Black-Scholes)
K = convert_to_actual_value(4.50)  # Investment needed for project (or strike price)
T = 2  # Time horizon for the decision (in years)
r = 0.05  # Risk-free rate (annualized)
sigma = 0.3  # Projected volatility of project returns (or stock price volatility)

option_value = black_scholes_call(S, K, T, r, sigma)

# Output the result
print("Real Options Valuation using Black-Scholes Model:\n")
print("Estimated Value of Business Decision (Option): ${:,.2f} million".format(option_value / 1000000))
