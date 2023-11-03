# Option Pricing Models in Valuation
# ----------------------------------
# Overview:
# Option Pricing Models are employed to assess the value of assets with option-like characteristics.
# The Black-Scholes Model is a well-known method used to calculate the theoretical price of European call and put options.
# Such a model can be adapted to value real assets like undeveloped land or patents under specific conditions.
#
# Desired Value:
# For assets like patents or undeveloped land, a higher option price suggests greater potential value in 
# the future when the option is exercised. Conversely, a low value might indicate limited potential or 
# higher uncertainty about future returns.
#
# Note: This script uses hard-coded values. For real-world application, data and assumptions should be adjusted.

import math
from scipy.stats import norm

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def black_scholes_call(S, K, T, r, v):
    """Calculate the Black-Scholes price for a European call option."""
    d1 = (math.log(S/K) + (r + 0.5 * v**2) * T) / (v * math.sqrt(T))
    d2 = d1 - v * math.sqrt(T)
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

# Hard-coded values for demonstration:
S = convert_to_actual_value(10.00)  # Current value of the asset (e.g., undeveloped land)
K = convert_to_actual_value(12.00)  # Strike price or exercise price
T = 3  # Time to expiration in years
r = 0.05  # Annual risk-free rate
v = 0.25  # Volatility of the asset's returns

call_option_price = black_scholes_call(S, K, T, r, v)

# Output the result
print("Option Pricing Models in Valuation (Black-Scholes Model):\n")
print("Value of the Call Option: ${:,.2f} million".format(call_option_price / 1000000))

